#include <SPI.h>
#include <Ethernet.h>
#include <LiquidCrystal.h>
#include <ArduinoJson.h>
#include <WebSocketClient.h>

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
char* server_ws;

//Ports
int port_http;
int port_ws;

//Creation des clients
EthernetClient client_http;
WebSocketClient client_ws;

//Buffer JSON
StaticJsonBuffer<200> jsonBuffer;
char json[] = "";



void onOpen(WebSocketClient client) 
{
  Serial.println("EXAMPLE: onOpen()");
}

void onMessage(WebSocketClient client, char* message) 
{
  Serial.println("EXAMPLE: onMessage()");
  Serial.print("Received: "); Serial.println(message);
}

void onError(WebSocketClient client, char* message) 
{
  Serial.println("EXAMPLE: onError()");
  Serial.print("ERROR: "); Serial.println(message);
}

int read_LCD_buttons()
{
  adc_key_in = analogRead(0); // Lire les valeurs du capteurs
  // Les valeurs renvoyées sont sensés etre: 0, 144, 329, 504, 741
  // Il y a une erreur possible de 50
  if (adc_key_in > 1000) return btnNONE; // Nous découpons les valeurs possibles en zone pour chaque bouton
  if (adc_key_in < 50) return btnRIGHT;
  if (adc_key_in < 250) return btnUP;
  if (adc_key_in < 450) return btnDOWN;
  if (adc_key_in < 650) return btnLEFT;
  if (adc_key_in < 850) return btnSELECT;
  return btnNONE; // On renvoie cela si l'on est au dessus de 850
}



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
    
    Serial.print("receptionJsonS : ");  // {"IP":"192.168.0.1","port":8000}
    Serial.println(receptionJsonS);
    
    int tailleJson = 100;
    //int tailleJson = sizeof(receptionJsonS)*2 + 2 ;
    Serial.print("tailleJson : ");
    Serial.println(tailleJson);
    
    char receptionJsonC[tailleJson];
    receptionJsonS.toCharArray(receptionJsonC,tailleJson);
    
    JsonObject& root = jsonBuffer.parseObject(receptionJsonC);
    
    const char* server_ws_tempo = root["IP"];
    port_ws = root["port"];
    
    server_ws = strdup(server_ws_tempo);
    
    Serial.print("server_ws : ");
    Serial.println(server_ws);
    Serial.print("port_ws : ");
    Serial.println(port_ws);
  
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
}

void loop()
{
  lcd.setCursor(0,1); // Placer le curseur au début de la seconde ligne
  lcd_key = read_LCD_buttons(); // Lire les boutons
  
  client_ws.monitor();
  
  switch (lcd_key) // Selon le bouton appuyer
  {
    case btnRIGHT: // Pour le bouton "Right"
    {
      lcd.print("RIGHT "); // Afficher "Right"
      client_ws.send("RIGHT!");
      break;
    }
    case btnLEFT: // Pour le bouton "left"
    {
      lcd.print("LEFT "); // Afficher "Left"
      client_ws.send("LEFT");
      break;
    }
  }
}


