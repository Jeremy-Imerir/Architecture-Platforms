#include "Arduino.h"
#include <Ethernet.h>
#include <SPI.h>
//#include <WebSocketClient.h>
#include "WebSocketClient.h"

//Partie pour Arduino
byte mac[]= { 0x98, 0x4F, 0xEE, 0x05, 0x37, 0x3C };
IPAddress ipArd(172, 30, 0, 225);

//Partie pour serveur
char server[]= "172.30.0.170";
int port= 8000;
IPAddress gateway(172,30,0,170);
IPAddress dns(0,0,0,0);
IPAddress subnet(255, 255, 254, 0);

WebSocketClient client;

void setup() {
  Serial.begin(9600);
  Serial.println("EXAMPLE: setup()");
  //Ethernet.begin(mac);
  //Ethernet.begin(mac, ipArd);
  //Ethernet.begin(mac, ipArd, dns,);
  //Ethernet.begin(mac, ipArd, dns, gateway);
  //Ethernet.begin(mac, ipArd, dns, gateway, subnet);
  
  client.connect(server, port);
  client.onOpen(onOpen);
  client.onMessage(onMessage);
  client.onError(onError);
  client.send("Hello Brice!");
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
