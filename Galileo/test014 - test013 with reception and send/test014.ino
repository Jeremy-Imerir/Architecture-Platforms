#include <SPI.h>
#include <Ethernet.h>
#include <LiquidCrystal.h>
#include <WebSocketClient.h> // from mauromezze https://github.com/mauromezze/IntelGalileo-SpacebrewWebsocket
#include <aJSON.h>           // Copyright (c) 2010, Interactive Matter, Marcus Nowotny https://github.com/interactive-matter/aJson

// LCD
LiquidCrystal lcd(8, 9, 4, 5, 6, 7);
int lcd_key = 0;
int adc_key_in = 0;
#define btnRIGHT 0
#define btnUP 1
#define btnDOWN 2
#define btnLEFT 3
#define btnSELECT 4
#define btnNONE 5

//Galileo
byte mac[]= { 0x98, 0x4F, 0xEE, 0x05, 0x37, 0x3C };
IPAddress ipArd ;

//Ip Serveurs
IPAddress server_http;
char server_ws[15];

//Ports
int port_http;
int port_ws;

//Creation des clients
EthernetClient client_http;
WebSocketClient client_ws;

//JSON
String messageS= 0;
int tailleMessage = 300;
char messageC[300];

char jsonString[] = "{\"cab\": {\"position\":{ \"x\": 5, \"y\": 5},\"goTo\": \"vertex\",\"status\": \"busy\",\"distanceToEnd\": 50}}";
char jsonString2[]= "{\"cabRequest\": {\"area\": \"areaname\",\"from\": \"a\",\"to\": \"b\"}}";
//variables modifié par le json
String ipS = 0;
int portI = 0;

String cabS = 0;
String positionS = 0;
int xI = 0;
int yI = 0;
String goToS = 0;
String statusS = 0;
int distanceToEndI = 0;

String cabRequestS = 0;
String areaS = 0;
String fromS = 0;
String toS = 0;

//clients
boolean clientPresent = false;

int read_LCD_buttons();
void onOpen(WebSocketClient client);
void onMessage(WebSocketClient client, char* message);
void onError(WebSocketClient client, char* message);
void parseJson(char *jsonString) ;
void etatTaxi();
void nettoyageLcd();



void setup() 
{  
  lcd.begin(16, 2); // Démarrer la librairie
  lcd.setCursor(0,0); // Placer le curseur au début de la première ligne
  lcd.print("Initialisation"); // Afficher un message simple
  
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  server_http = * new IPAddress(192,168,0,1);
  ipArd       = * new IPAddress(192,168,0,2);
  port_http   = 8090;
  
  // start the Ethernet connection:
  Ethernet.begin(mac,ipArd);
  // give the Ethernet shield a second to initialize:
  delay(1000);
  Serial.println("connecting...");
  // Verification de l'adresse IP du galileo
  Serial.print("IP : ");
  Serial.println( Ethernet.localIP());
  // if you get a connection, report back via serial:  
  
  
  
  if (client_http.connect(server_http, port_http)) 
  {
    Serial.println("connected");
    // Make a HTTP request:
    client_http.println("GET /");
    client_http.println();
   
    String receptionJsonS;
    
    while (client_http.available()) 
    {
      char c = client_http.read();
      receptionJsonS += c;
    }
    
    Serial.println("disconnecting http...");
    client_http.stop();
    
    //String receptionJsonS; //Pour test sans serveur
    //receptionJsonS = "{\"IP\":\"192.168.0.1\",\"port\":8000}"; //Pour test sans serveur
    
    Serial.print("receptionJsonS : ");  // {"IP":"192.168.0.1","port":8000}
    Serial.println(receptionJsonS);
    
    //int tailleJson = sizeof(receptionJsonS)+ 1; // +1 pour le fin de caractère
    int tailleJson = 100;
    Serial.print("tailleJson : ");
    Serial.println(tailleJson);
    
    char receptionJsonC[tailleJson];
    receptionJsonS.toCharArray(receptionJsonC,tailleJson);
    
    parseJson (receptionJsonC);
    
    ipS.toCharArray(server_ws, 15);
    port_ws = portI;
    
    Serial.print("IP : ");
    Serial.println(server_ws);
    Serial.print("Port : ");
    Serial.println(port_ws);
    
    delay(1000);
    
    client_ws.connect(server_ws, port_ws);
    Serial.println("connecting WebSocket...");
    client_ws.onOpen(onOpen);
    client_ws.onMessage(onMessage);
    client_ws.onError(onError);
    
  } 
  else 
  {
    // if you didn't get a connection to the server:
    Serial.println("connection http failed");
  }
  
  //sert a nettoyer l'écran
  nettoyageLcd();
}

void loop()
{
  
  nettoyageLcd();
  etatTaxi();
  
  if(clientPresent == false)
  {
    client_ws.monitor();
    client_ws.onMessage(onMessage);
    
    //Test en dur en cas de rupture serveur.
    //messageS = "{\"cabRequest\": {\"area\": \"areaname\",\"from\": \"a\",\"to\": \"b\"}}";
    //messageS = "{\"cab\": {\"x\": 0, \"y\": 1,\"goTo\": \"\" ,\"status\": \"Free\",\"distanceToEnd\": 0}}";
    
    messageS.toCharArray(messageC,tailleMessage);
    parseJson (messageC);
    
    for (int i = 0; i < tailleMessage ; i++)
    {
      if (messageC[i]=='R' && messageC[i+1]=='e' && messageC[i+2]=='q' && messageC[i+3]=='u')
      {
        clientPresent = true;
        i = tailleMessage - 1;
      }
    }
    
  }
  else
  {
    lcd_key = read_LCD_buttons();
    switch (lcd_key) // Selon le bouton appuyer
    {
      case btnRIGHT: // Pour le bouton accepter
      {
        client_ws.send(messageC);
        messageS = 0;
        clientPresent = false;
        delay(1500); // Evite d'appuyer plusieurs fois dessus le bouton .
        break;
      }
      case btnLEFT: // Pour le bouton refuser
      {
        //client_ws.send("refuse");
        messageS = 0;
        clientPresent = false;
        delay(1500); // Evite d'appuyer plusieurs fois dessus le bouton .
        break;
      }
    }
  }
}
  
  

int read_LCD_buttons()
{
  adc_key_in = analogRead(0); // Lire les valeurs du capteurs
  // Les valeurs renvoyées sont sensés etre: 0, 144, 329, 504, 741
  // Il y a une erreur possible de 50
  if (adc_key_in > 1000) return btnNONE; // Nous découpons les valeurs possibles en zone pour chaque bouton
  else if (adc_key_in < 50) return btnRIGHT;
  else if (adc_key_in < 250) return btnUP;
  else if (adc_key_in < 450) return btnDOWN;
  else if (adc_key_in < 650) return btnLEFT;
  else if (adc_key_in < 850) return btnSELECT;
  return btnNONE; // On renvoie cela si l'on est au dessus de 850
}

void onOpen(WebSocketClient client) 
{
  Serial.println("EXAMPLE: onOpen()");
}

void onMessage(WebSocketClient client, char* message) 
{
  Serial.println("EXAMPLE: onMessage()");
  Serial.print("Received: "); Serial.println(message);
  
  //Sauvegarde du message dans une variable global, sert à l'analyse.
  messageS = message;
}

void onError(WebSocketClient client, char* message) 
{
  Serial.println("EXAMPLE: onError()");
  Serial.print("ERROR: "); Serial.println(message);
}

void parseJson(char *jsonString) 
{
    aJsonObject* root = aJson.parse(jsonString);

    if (root != NULL) 
    {
        // trame :  {"IP":"192.168.0.1","port":8000}
        aJsonObject* ip = aJson.getObjectItem(root, "ip");
        if(ip != NULL) { ipS = ip -> valuestring ; }
        aJsonObject* port = aJson.getObjectItem(root, "port");
        if(port != NULL) { portI = port -> valueint ; }
      
        // trame : {"cab": {"position":{ "x": 5, "y": 5},"goTo": "vertex","status": "busy","distanceToEnd": 50}}
        // trame : {"cab": {"x": 5, "y": 5,"goTo": "vertex","status": "busy","distanceToEnd": 50}}
        // trame : {"cab": {"x": 0, "y": 1,"goTo": ""      ,"status": "Free","distanceToEnd":   }}

        aJsonObject* cab = aJson.getObjectItem(root, "cab");
        if (cab != NULL) 
        {
            cabS = cab -> valuestring;
            //aJsonObject* position = aJson.getObjectItem(cab, "position");
            aJsonObject* goTo = aJson.getObjectItem(cab, "goTo");
            aJsonObject* status = aJson.getObjectItem(cab, "status");
            aJsonObject* distanceToEnd = aJson.getObjectItem(cab, "distanceToEnd");
            aJsonObject* x = aJson.getObjectItem(cab, "x");
            aJsonObject* y = aJson.getObjectItem(cab, "y");
            if(x != NULL) { xI = x -> valueint ; }
            if(y != NULL) { yI = y -> valueint ; }
            /*if (position != NULL)
            {
                positionS = position -> valuestring;
                aJsonObject* x = aJson.getObjectItem(position, "x");
                aJsonObject* y = aJson.getObjectItem(position, "y");
                if(x != NULL) { xI = x -> valueint ; }
                if(y != NULL) { yI = y -> valueint ; }
            }*/
            if(goTo != NULL) { goToS = goTo -> valuestring ; }
            if(status != NULL) { statusS = status -> valuestring ; }
            if(distanceToEnd != NULL) { distanceToEndI = distanceToEnd -> valueint ; }
        }
        // trame : {"cabRequest": {{"area": "areaname","from": "a","to": "b"}}}
        aJsonObject* cabRequest = aJson.getObjectItem(root, "cabRequest");
        if (cabRequest != NULL) 
        {
            cabRequestS = cabRequest -> valuestring;
            aJsonObject* area = aJson.getObjectItem(cabRequest, "area");
            aJsonObject* from = aJson.getObjectItem(cabRequest, "from");
            aJsonObject* to = aJson.getObjectItem(cabRequest, "to");
            
            if(area != NULL) { areaS = area -> valuestring ; }
            if(from != NULL) { fromS = from -> valuestring ; }
            if(to   != NULL) { toS   = to   -> valuestring ; }
        }
    }
}

void etatTaxi()
{
   if(clientPresent == false)
   {
     lcd.setCursor(0,0);
     lcd.print("status : ");
     lcd.setCursor(7,0);
     lcd.print(statusS);
     lcd.setCursor(0,1); 
     lcd.print("x");
     lcd.setCursor(1,1);
     lcd.print(xI);
     lcd.setCursor(4,1);
     lcd.print("y");
     lcd.setCursor(5,1);
     lcd.print(yI);
     lcd.setCursor(8,1);
     lcd.print("DTE");
     lcd.setCursor(12,1);
     lcd.print(distanceToEndI);
   }
   else
   {
     lcd.setCursor(0,0);
     lcd.print("Client O/N");
     lcd.setCursor(0,1);
     lcd.print("From");
     lcd.setCursor(5,1);
     lcd.print(fromS);
     lcd.setCursor(8,1);
     lcd.print("to");
     lcd.setCursor(11,1);
     lcd.print(toS);    
   }
}

void nettoyageLcd()
{
  for (int i = 0; i<2 ; i++)
  {
    for (int j = 0; j<16 ; j++)
    {
       lcd.setCursor(j,i);
       lcd.print(" ");
    }
  }
}

