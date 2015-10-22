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

//Ip Serveurs // Servers IP
IPAddress server_http;
char server_ws[15];

//Ports
int port_http;
int port_ws;

//Creation des clients // Clients creations
EthernetClient client_http;
WebSocketClient client_ws;

//JSON
String messageS= 0;
int MessageSize = 300;
char messageC[300];

char jsonString[] = "{\"cab\": {\"position\":{ \"x\": 5, \"y\": 5},\"goTo\": \"vertex\",\"status\": \"busy\",\"distanceToEnd\": 50}}";
char jsonString2[]= "{\"cabRequest\": {\"area\": \"areaname\",\"from\": \"a\",\"to\": \"b\"}}";
//variables modifié par le json // variables modificated by json
String ipS = 0;
int portI = 0;

String cabS = 0;
String positionS = 0;
int xI = 0;
int yI = 0;
float xF = 0;
float yF = 0;
String goToS = 0;
String statusS = 0;
int distanceToEndI = 0;
float distanceToEndF = 0;

String cabRequestS = 0;
String areaS = 0;
String fromS = 0;
String toS = 0;

//clients
boolean clientPresent = false;


//Déclaration des fonctions // Fonctions declaration
int read_LCD_buttons();
void onOpen(WebSocketClient client);
void onMessage(WebSocketClient client, char* message);
void onError(WebSocketClient client, char* message);
void parseJson(char *jsonString) ;
void etatTaxi();
void nettoyageLcd();
void init_http();
