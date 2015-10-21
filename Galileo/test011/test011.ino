#include <aJSON.h>

String queryS = 0;
int countI = 0;
String createdS = 0;
String langS = 0;
String resultsS = 0;
String itemS = 0;
String titleS = 0;

// function definitions
void parseJson(char *jsonString) ;

// Json string to parse
char jsonString[] = "{\"query\":{\"count\":1,\"created\":\"2012-08-04T14:46:03Z\",\"lang\":\"en-US\",\"results\":{\"item\":{\"title\":\"Handling FTP usernames with @ in them\"}}}}";

void setup() {
    Serial.begin(9600);
    Serial.println(jsonString);
    Serial.println("Starting to parse");

    parseJson(jsonString);
    
    Serial.print("query : ");
    Serial.println(queryS);
    Serial.print("count : ");
    Serial.println(countI);
    Serial.print("created : ");
    Serial.println(createdS);
    Serial.print("lang : ");
    Serial.println(langS);
    Serial.print("results : ");
    Serial.println(resultsS);
    Serial.print("item : ");
    Serial.println(itemS);
    Serial.print("title : ");
    Serial.println(titleS);
}

/**
 * Parse the JSON String. Uses aJson library
 * 
 * Refer to http://hardwarefun.com/tutorials/parsing-json-in-arduino
 */
void parseJson(char *jsonString) 
{
    aJsonObject* root = aJson.parse(jsonString);

    if (root != NULL) {
        //Serial.println("Parsed successfully 1 " );
        aJsonObject* query = aJson.getObjectItem(root, "query");

        if (query != NULL) {
            //Serial.println("Parsed successfully 2 " );
             
            queryS = query-> valuestring;
            aJsonObject* count = aJson.getObjectItem(query, "count");
            aJsonObject* created = aJson.getObjectItem(query, "created");
            aJsonObject* lang = aJson.getObjectItem(query, "lang");   
            aJsonObject* results = aJson.getObjectItem(query, "results");
            
            if (count != NULL) {countI = count -> valueint;}
            if (created != NULL) {createdS = created -> valuestring;}
            if (lang != NULL) {langS = lang -> valuestring;}

            if (results != NULL) {
                //Serial.println("Parsed successfully 3 " );
                resultsS = results -> valuestring;
                aJsonObject* item = aJson.getObjectItem(results, "item"); 

                if (item != NULL) {
                    itemS = item -> valuestring;
                    //Serial.println("Parsed successfully 4 " );
                    aJsonObject* title = aJson.getObjectItem(item, "title"); 
                    
                    if (title != NULL) {
                        //Serial.println("Parsed successfully 5 " );
                        titleS = title->valuestring;
                    }
                }
            }
        }
    }
}

void loop() {
   // Nothing to do 
   ;
}
