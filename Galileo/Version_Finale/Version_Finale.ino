//#include <SPI.h>
#include <Ethernet.h>
#include <LiquidCrystal.h>
#include <WebSocketClient.h> // from mauromezze https://github.com/mauromezze/IntelGalileo-SpacebrewWebsocket
#include <aJSON.h>           // Copyright (c) 2010, Interactive Matter, Marcus Nowotny https://github.com/interactive-matter/aJson

#include "Variables_Globales.h" //all globales variables.


void setup() 
{  
  
  init_http();
  
  if (client_http.connect(server_http, port_http)) //Si on est bien connecté au serveur // if we are connect with the server
  {
    Serial.println("connected");
    client_http.println("GET /"); //Fait la requette http // Make a HTTP request:
    client_http.println();
   
    String receptionJsonHttpS;  
    
    while (client_http.available()) 
    {
      char c = client_http.read();
      receptionJsonHttpS += c;        // lecture et sauvegarde du get // read & save of get
    }
    
    client_http.stop();         // Stop du client http // Stop of http client
    Serial.println("disconnecting http...");
    
    //Pour test sans serveur // for test without server
    //String receptionJsonS; 
    //receptionJsonS = "{\"IP\":\"192.168.0.1\",\"port\":8000}";
    
    //Verification du get // Get verification
    Serial.print("receptionJsonS : ");
    Serial.println(receptionJsonHttpS);
    
    //int tailleJson = sizeof(receptionJsonS)+ 1; // +1 pour le fin de caractère
    //Serial.print("tailleJson : ");  
    //Serial.println(tailleJson);
    int JsonSize = 100;    // problème avec sizeof() // 100 because problem with sizeof().
    
    char receptionJsonC[JsonSize];
    receptionJsonHttpS.toCharArray(receptionJsonC,JsonSize);  //String to char[]
    
    parseJson (receptionJsonC);
    
    ipS.toCharArray(server_ws, 15);   //String to char[] & ip du json dans l'ip server_ws // ip with json to server_ws
    port_ws = portI;                  //Attribution du port_ws par le port du json        // port with json to port_ws
    
    // Verification du parseJson // parseJson verification
    Serial.print("IP : ");
    Serial.println(server_ws);
    Serial.print("Port : ");
    Serial.println(port_ws);
    
    delay(1000); // attendre une sec // wait a second for be safe.
    
    //Connexion au serveur ws // connection with server ws
    client_ws.connect(server_ws, port_ws);
    Serial.println("connecting WebSocket...");
    client_ws.onOpen(onOpen);
    client_ws.onMessage(onMessage);
    client_ws.onError(onError);
  } 
  else 
  {
    // Pas de connexion au serveur http // if you didn't get a connection to the server:
    Serial.println("connection http failed");
  }
  
  //sert a nettoyer l'écran // clear the lcd
  nettoyageLcd();
}

void loop()
{
  
  nettoyageLcd(); 
  etatTaxi();      //Affiche divers informations // display various informations.
  
  if(clientPresent == false)
  {
    client_ws.monitor();            // Utile pour // usefull for connect / re-connect / disconnect / message  ... but for a unknow reason a big latence.
    client_ws.onMessage(onMessage); // can be commented
    
    //Test en dur en cas de rupture serveur.MessageSize
    //messageS = "{\"cabRequest\": {\"area\": \"areaname\",\"from\": \"a\",\"to\": \"b\"}}";
    //messageS = "{\"cab\": {\"x\": 0, \"y\": 1,\"goTo\": \"\" ,\"status\": \"Free\",\"distanceToEnd\": 0}}";
    
    messageS.toCharArray(messageC,MessageSize);      // Message string-> char[]
    parseJson (messageC);                            // ParseJson
    
    for (int i = 0; i < MessageSize ; i++)         // Verification s'il s'agit d'un cab ou d'un cabRequest // verification if is a cab or cabRequest
    {
      if (messageC[i]=='R' && messageC[i+1]=='e' && messageC[i+2]=='q' && messageC[i+3]=='u')  // if "Requ" -> cabRequest .
      {
        clientPresent = true;    // client present
        i = MessageSize - 1;   // fin de boucle // for end.
      }
    }
    
  }
  else
  {
    lcd_key = read_LCD_buttons();  //lire les valeurs des boutons // read LCD buttons
    switch (lcd_key) // Selon le bouton appuyer  // switch for button press.
    {
      case btnRIGHT: // Pour le bouton accepter  // For accept button
      {
        client_ws.send(messageC);      // Renvois de la trame pour accepter // return trame for accept
        messageS = 0;                  // init message.
        clientPresent = false;         // reset clientPresent.
        delay(1500);                   // Evite d'appuyer plusieurs fois dessus le bouton.
        break;
      }
      case btnLEFT: // Pour le bouton refuser
      {
        //client_ws.send("refuse");    // Sers a refuser le client ... pour le momment pas de renvois = refuser ...
        messageS = 0;                  // init message.
        clientPresent = false;         // reset clientPresent.
        delay(1500);                   // Evite d'appuyer plusieurs fois dessus le bouton.
        break;
      }
    }
  }
}
  
  

int read_LCD_buttons()
{
  adc_key_in = analogRead(0); // Lire les valeurs du capteurs // Read sensors.
  // Les valeurs renvoyées sont sensés etre: 0, 144, 329, 504, 741 //  values are supposed to be : 0, 144, 329, 504, 741.
  // Il y a une erreur possible de 50 // maybe a error of 50 pts.
  if (adc_key_in > 1000) return btnNONE;         // Nous découpons les valeurs possibles en zone pour chaque bouton //  cut values and attribut name. 
  else if (adc_key_in < 50)  return btnRIGHT;
  else if (adc_key_in < 250) return btnUP;
  else if (adc_key_in < 450) return btnDOWN;
  else if (adc_key_in < 650) return btnLEFT;
  else if (adc_key_in < 850) return btnSELECT;
  return btnNONE; // On renvoie cela si l'on est au dessus de 850 // return btnNONE if > 850.
}

void onOpen(WebSocketClient client) 
{
  Serial.println("EXAMPLE: onOpen()");
}

void onMessage(WebSocketClient client, char* message) 
{
  Serial.println("EXAMPLE: onMessage()");
  Serial.print("Received: "); Serial.println(message);
  messageS = message; //Sauvegarde du message dans une variable global, sert à l'analyse. // save in global variable, use for analysis.
}

void onError(WebSocketClient client, char* message) 
{
  Serial.println("EXAMPLE: onError()");              
  Serial.print("ERROR: "); Serial.println(message);  
}

void parseJson(char *jsonString) 
{
    aJsonObject* root = aJson.parse(jsonString);    //Creation de root, utiliser comme premier parent // creation of root, use like parent.

    if (root != NULL) 
    {
        // trame :  {"IP":"192.168.0.1","port":8000}
        aJsonObject* ip = aJson.getObjectItem(root, "ip");        // name of aJsonObject = fonction (parent, name of Json).
        if(ip != NULL) { ipS = ip -> valuestring ; }              // if different of null, global variable = value of json, int or string.
        aJsonObject* port = aJson.getObjectItem(root, "port");    // same for all rest of the fonction.
        if(port != NULL) { portI = port -> valueint ; }
      
        // trame : {"cab": {"position":{ "x": 5, "y": 5},"goTo": "vertex","status": "busy","distanceToEnd": 50}}
        // trame : {"cab": {"x": 5, "y": 5,"goTo": "vertex","status": "busy","distanceToEnd": 50}}
        // trame : {"cab": {"x": 0, "y": 1,"goTo": ""      ,"status": "Free","distanceToEnd":  0}}

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
            /*if(x != NULL) { xI = x -> valueint ; }
            if(y != NULL) { yI = y -> valueint ; }*/
            if(x != NULL) { xF = x -> valuefloat ; }
            if(y != NULL) { yF = y -> valuefloat ; }
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
   //Si nous n'avons pas de demande de client, afficher les informations de base // if we haven't a new client request, display basic information.
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
   else // Ou nous avons un client et affiche ces informations // or we have a client and display this informations
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
  //assigne un espace à chaque case // add a space every case.
  for (int i = 0; i<2 ; i++)
  {
    for (int j = 0; j<16 ; j++)
    {
       lcd.setCursor(j,i);
       lcd.print(" ");
    }
  }
}

void init_http()
{
  lcd.begin(16, 2);             // Démarrer la librairie                             // Start lcd .
  lcd.setCursor(0,0);           // Placer le curseur au début de la première ligne   // set cursor on first case, in first line.
  lcd.print("Initialisation");  // Afficher un message simple                        // simple message on lcd
  
  // Début de la communication série & attribution des adresses. // Open serial communications and add new IPAddress.
  Serial.begin(9600);
  server_http = * new IPAddress(192,168,0,1);  // adresse ip du serveur // ip address of the server
  ipArd       = * new IPAddress(192,168,0,2);  // adresse ip du galileo // ip address of the galileo
  port_http   = 8090;                          // port du serveur html  // html port server
  
  // Début de la connexion Ethernet // start the Ethernet connection:
  Ethernet.begin(mac,ipArd);
  // un delay de 1 seconde pour l'initialisation // give the Ethernet shield a second to initialize:
  delay(1000);
  // Verification des variables // Verification of variables
  Serial.print("Ip server_http : ");
  Serial.println(server_http);
  Serial.print("Port_http : ");
  Serial.println(port_http);
  Serial.print("Ip arduino : ");
  Serial.println(ipArd);
  
  Serial.println("connecting...");  
}

