#include <Ethernet.h>
#include <SPI.h>


byte mac[] = { 0x98, 0x4F, 0xEE, 0x05, 0x37, 0x3C }; // adresse Mac du galileo
byte ip[] = { 10, 0, 0, 177 }; // adresse IP que l'on donne au galileo
byte server[] = { 64, 233, 187, 99 }; // adresse iP du serveur

EthernetClient client;

void setup()
{
  Ethernet.begin(mac, ip); // initialize the ethernet device // begin(mac, ip, gateway, subnet);
  Serial.begin(9600);

  delay(1000); // Attendre 1 sec

  Serial.println("connecting..."); // Afficher "connecting..." tant qu'il n'y a pas de connexion

  // Si le client se connect au serveur port 80
  if (client.connect(server, 80)) // client.connect(ip, port) ou client.connect(url, port)
  {
    Serial.println("connected");
    client.println("GET /search?q=arduino HTTP/1.0");
    client.println();
  } 
  else // Pas de connexion
  {
    Serial.println("connection failed");
  }
}

void loop()
{
  if (client.available()) 
  {
    char c = client.read();
    Serial.print(c);
  }

  if (!client.connected()) 
  {
    Serial.println();
    Serial.println("disconnecting.");
    client.stop();
    for(;;)
      ;
  }
}
