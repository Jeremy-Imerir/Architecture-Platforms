#include <aJSON.h>

// function definitions
void parseJson(char *jsonString) ;

// Json string to parse
//char jsonString[] = "{\"cab\": [\"position\":{ \"x\": 5, \"y\": 5},\"goTo\": \"vertex\",\"status\": \"busy\",\"distanceToEnd\": 50]}";
char jsonString[] = "{\"cab\": {\"position\":{ \"x\": 5, \"y\": 5},\"goTo\": \"vertex\",\"status\": \"busy\",\"distanceToEnd\": 50}}";
//char jsonString2[]= "{\"cabRequest\": {{\"area\": \"areaname\",\"from\": \"a\",\"to\": \"b\"}}}";
char jsonString2[]= "{\"cabRequest\": {\"area\": \"areaname\",\"from\": \"a\",\"to\": \"b\"}}";

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

void setup() {
    Serial.begin(9600);
    
    Serial.println(jsonString);
    Serial.println("Starting to parse");
    Serial.println();
    parseJson(jsonString);
    Serial.print("cab : ");
    Serial.println(cabS);
    Serial.print("position : ");
    Serial.println(positionS);
    Serial.print("x : ");
    Serial.println(xI);
    Serial.print("y : ");
    Serial.println(yI);
    Serial.print("goTo : ");
    Serial.println(goToS);
    Serial.print("status : ");
    Serial.println(statusS);
    Serial.print("distanceToEnd : ");
    Serial.println(distanceToEndI);
    
    Serial.println();
    
    Serial.println(jsonString2);
    Serial.println("Starting to parse");
    Serial.println();
    parseJson(jsonString2);
    Serial.print("cabRequest : ");
    Serial.println(cabRequestS);
    Serial.print("area : ");
    Serial.println(areaS);
    Serial.print("from : ");
    Serial.println(fromS);
    Serial.print("to : ");
    Serial.println(toS);
    
}

void parseJson(char *jsonString) 
{
    aJsonObject* root = aJson.parse(jsonString);

    if (root != NULL) 
    {
        // trame : {"cab": {"position":{ "x": 5, "y": 5},"goTo": "vertex","status": "busy","distanceToEnd": 50}}
        aJsonObject* cab = aJson.getObjectItem(root, "cab");
        if (cab != NULL) 
        {
            cabS = cab -> valuestring;
            aJsonObject* position = aJson.getObjectItem(cab, "position");
            aJsonObject* goTo = aJson.getObjectItem(cab, "goTo");
            aJsonObject* status = aJson.getObjectItem(cab, "status");
            aJsonObject* distanceToEnd = aJson.getObjectItem(cab, "distanceToEnd");
            
            if (position != NULL)
            {
                positionS = position -> valuestring;
                aJsonObject* x = aJson.getObjectItem(position, "x");
                aJsonObject* y = aJson.getObjectItem(position, "y");
                if(x != NULL) { xI = x -> valueint ; }
                if(y != NULL) { yI = y -> valueint ; }
            }
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
            if(to != NULL)   { toS = to -> valuestring ; }
        }
    }
}

void loop() {
   // Nothing to do 
   ;
}
