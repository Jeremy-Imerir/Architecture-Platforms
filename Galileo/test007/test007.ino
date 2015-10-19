#include "Arduino.h"
#include <Ethernet.h>
#include <SPI.h>
//#include <WebSocketClient.h>
#include "WebSocketClient.h"
#include <ArduinoJson.h>

//Partie pour Arduino
byte mac[]= { 0x98, 0x4F, 0xEE, 0x05, 0x37, 0x3C };
IPAddress ipArd(172, 30, 0, 230);

//Partie pour serveur
char server[]= "172.30.0.170";
int port= 8000;
IPAddress gateway(172,30,0,170);
IPAddress dns(172,30,0,171);
IPAddress subnet(255, 255, 255, 0);

//Json
//Reserve de l'espace mémoire
StaticJsonBuffer<200> jsonBuffer;
//Tableau pour simuler le Json
char json[] =  
      "{\"sensor\":\"gps\",\"time\":1351824120,\"data\":{ \"da\": [48.756080,2.302038] } }";

WebSocketClient client;  

void setup() {
  //9600 bauds
  Serial.begin(9600);
  Serial.println("EXAMPLE: setup()");
  
  //Suivant les infos renseigné
  //Ethernet.begin(mac);
  //Ethernet.begin(mac, ipArd);
  //Ethernet.begin(mac, ipArd, dns,);
  //Ethernet.begin(mac, ipArd, dns, gateway);
  Ethernet.begin(mac, ipArd, dns, gateway, subnet);
  
  //Connexion au server
  client.connect(server, port);
  client.onOpen(onOpen);
  //Reception d'un message
  client.onMessage(onMessage);
  client.onError(onError);
  //Envois d'un message
  client.send("Hello Brice!");
  
  //Deserialize the JSON string
  JsonObject& root = jsonBuffer.parseObject(json);
  //Remplir les variables a partir du JSON
  const char* sensor = root["sensor"];
  long time = root["time"];
  double latitude = root["data"][0]["da"];
  double longitude = root["data"][1];
  //Afficher la valeur des variables
  Serial.println(sensor);
  Serial.println(time);
  Serial.println(latitude, 6);
  Serial.println(longitude, 6);

}

void loop() {
  client.monitor();
}

void onOpen(WebSocketClient client) {
  Serial.println("EXAMPLE: onOpen()");
}

void onMessage(WebSocketClient client, char* message) {
  Serial.println("EXAMPLE: onMessage()");
  Serial.print("Received: "); Serial.println(message);
}

void onError(WebSocketClient client, char* message) {
  Serial.println("EXAMPLE: onError()");
  Serial.print("ERROR: "); Serial.println(message);
}
