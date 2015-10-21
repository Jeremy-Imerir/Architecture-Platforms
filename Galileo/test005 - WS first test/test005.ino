#include "Arduino.h"
#include <Ethernet.h>
#include <SPI.h>
//#include <WebSocketClient.h>
#include "WebSocketClient.h"

//Partie pour Ethernet
byte mac[]= { 0x98, 0x4F, 0xEE, 0x05, 0x37, 0x3C };
IPAddress ipArd(192, 168, 1, 224);
IPAddress gateway(192, 168, 1, 1);
IPAddress dns(192, 168, 1, 1);
IPAddress subnet(255, 255, 255, 0);

//Partie pour Client
char server[]= "192.168.1.50";
int port= 2009;

WebSocketClient client;

void setup() {
  Serial.begin(9600);
  Serial.println("EXAMPLE: setup()");
  //Ethernet.begin(mac);
  Ethernet.begin(mac,ipArd,dns,gateway,subnet);
  //client.connect(server);
  client.connect(server,port);
  client.onOpen(onOpen);
  client.onMessage(onMessage);
  client.onError(onError);
  client.send("Hello Nico!");
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
