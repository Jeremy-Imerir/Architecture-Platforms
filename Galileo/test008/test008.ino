/*
  Web client
 
 This sketch connects to a website (http://www.google.com)
 using an Arduino Wiznet Ethernet shield. 
 
 Circuit:
 * Ethernet shield attached to pins 10, 11, 12, 13
 
 created 18 Dec 2009
 modified 9 Apr 2012
 by David A. Mellis
 
 */

#include <SPI.h>
#include <Ethernet.h>

// Enter a MAC address for your controller below.
// Newer Ethernet shields have a MAC address printed on a sticker on the shield
byte mac[]= { 0x98, 0x4F, 0xEE, 0x05, 0x37, 0x3C };

IPAddress server;
IPAddress ipArd ;

int port = 8080;

// Initialize the Ethernet client library
// with the IP address and port of the server 
// that you want to connect to (port 80 is default for HTTP):
EthernetClient client;

void setup() {
 // Open serial communications and wait for port to open:
  Serial.begin(9600);
  server = * new IPAddress(192,168,0,1);
  ipArd  = * new IPAddress(192,168,0,2);

  IPAddress ipArd (192,168,0,2);
  
  // start the Ethernet connection:
  Ethernet.begin(mac,ipArd);
 
  // give the Ethernet shield a second to initialize:
  delay(1000);
  Serial.println("connecting...");
  // Verification de l'adresse IP du galileo
  Serial.print("IP : ");
  Serial.println( Ethernet.localIP());
  // if you get a connection, report back via serial:  
  if (client.connect(server, port)) 
  {
    Serial.println("connected");
    // Make a HTTP request:
    client.println("GET /");
    client.println();
  } 
  else 
  {
    // if you didn't get a connection to the server:
    Serial.println("connection failed!!");
  }
}

void loop()
{
  // if there are incoming bytes available 
  // from the server, read them and print them:
  // {"IP":"172.30.0.227","port":8000}
  if (client.available()) 
  {
    char c = client.read();
    Serial.print(c);
  }

  // if the server's disconnected, stop the client:
  if (!client.connected()) {
    Serial.println();
    Serial.println("disconnecting.");
    client.stop();

    for(;;)
    {
    
    }
  }
}

