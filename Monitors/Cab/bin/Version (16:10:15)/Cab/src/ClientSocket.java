import java.awt.image.IndexColorModel;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Observable;
import java.util.Set;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.TimeUnit;

import org.eclipse.jetty.websocket.api.Session;
import org.eclipse.jetty.websocket.api.annotations.OnWebSocketClose;
import org.eclipse.jetty.websocket.api.annotations.OnWebSocketConnect;
import org.eclipse.jetty.websocket.api.annotations.OnWebSocketMessage;
import org.eclipse.jetty.websocket.api.annotations.WebSocket;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

@WebSocket(maxTextMessageSize = 64 * 1024)
public class ClientSocket extends Observable{

	private Session session;
	private String msg;
    HashMap <String, Areas> areas;
	
	/* declaration of variables */
	int nbQuartiers = 0;
    int w = 0;
    int h = 0;
    int tab[][] = null;
	
	/* socket message received */
	@OnWebSocketMessage
	public void onMessage(String message) throws IOException{
		System.out.println("Message received from server: " + message);
		this.msg = message;
		
		/* reads and interprets the JSON */
        readJSON(message);
        
//		setChanged();
//		notifyObservers(message);
	}
	
	/* socket connect */
	@OnWebSocketConnect
	public void onConnect(Session session){
		System.out.println("Connected to server: ");
		this.session = session;
		//sendMessage("{\"cmd\":\"areas\"}");
	}

	/* socket message sent */
	public void sendMessage(String str){
		try {
			session.getRemote().sendString(str);
		} catch (IOException e){
			e.printStackTrace();
		}
	}
	
	
	/* socket close */
//	@OnWebSocketClose
	public void onClose(int statusCode, String reason) {
        System.out.printf("Connection closed: %d - %s%n", statusCode, reason);
        this.session = null;
    }
	
	/**
	 * JSON
	 */
	public void readJSON(String message){
		/* creating objects and JSONParser JsonObject */
        JSONParser parser = new JSONParser();
        JSONObject jsonObject = null;
        try {
	    	jsonObject = (JSONObject) parser.parse(message);
	        
	    	/* creation of new areas */
	    	this.areas = new HashMap<String, Areas>();
	        for (JSONObject o: (ArrayList<JSONObject>) jsonObject.get("areas")){
	        	this.areas.put((String)o.get("name"), new Areas(o));
	        }
	        
	        
	        /* creating a JSON object list containing the parameters of the frame JSON ("areas") */
	        JSONArray areas = (JSONArray) jsonObject.get("areas");
	    	Iterator ite_areas = areas.iterator();
            
		    /* name */
            while (ite_areas.hasNext()) {
                JSONObject obj1 = (JSONObject) ite_areas.next();
                /* map */
                JSONObject map = (JSONObject) obj1.get("map");
                System.out.println(map);
                /* weight */
                JSONObject weight = (JSONObject) map.get("weight");
                
                /* obtains the values of w and h */
                Collection col_weight = weight.values();
                Iterator i = col_weight.iterator();
                System.out.println(i.next());
                
                
//                for( Object obj: col_weight) {
//                    /* creating a list of JSON objects containing the objects in the collection */
//                    ArrayList<JSONObject> keyl = (ArrayList<JSONObject>) obj;
////                    System.out.println(keyl.get(0));
//                }
                /* vertices */
                JSONArray vertices = (JSONArray) map.get("vertices");
//                System.out.println(vertices);
//                Iterator ite_vertices = vertices.iterator();
//                JSONObject obj2 = (JSONObject) ite_vertices.next();
//                
//                /* recovers the X and Y different points */
//                for(int i=0 ;i<vertices.size() ;i++){
//                	for(int j=0; j<vertices.size();j++){
//                		tab[i][j] = (double) obj2.get("x");
//                		j++;
//                		tab[i][j] = (double) obj2.get("y");
//                	}
//                }
                
                /* streets */
//                JSONArray streets = (JSONArray) jsonObject.get("streets");
//                Iterator ite_streets = streets.iterator();
//                
                /* bridges */
//                JSONArray bridges = (JSONArray) jsonObject.get("bridges");
//                Iterator ite_bridges = bridges.iterator();
                
                
                
                /* weight, vertices, streets and bridges */
//              Iterator ite_map = map.iterator();               
//              while (ite_map.hasNext()){
//              	JSONObject Obj2 = (JSONObject) ite_map.next();
//                  JSONArray weight = (JSONArray) Obj2.get("weight");
//                  JSONArray vertices = (JSONArray) Obj2.get("vertices");
//                  JSONArray streets = (JSONArray) Obj2.get("streets");
//                  JSONArray bridges = (JSONArray) Obj2.get("bridges");
                
            }

        

/***************VERSION FONCTIONNELLE********************/    
//		    for(JSONObject a: liste){
//	            /* we isolate the contents of objects in a collection */
//	          	Collection names = a.values();
//			    System.out.println("names: " + names + "\n");
//			    // get an array from the JSON object
//			                
//	        }
//            System.out.println("liste: " + liste + "\n");
//            for(JSONObject a: liste){
//                /* we isolate the contents of objects in a collection */
//            	Collection names = a.values();
//                System.out.println("names: " + names + "\n");
//                /* for all objects in the collection */
//                for(Object obj: names) {
//                	Iterator itNames = names.iterator();
//                }
//            }
/********************************************************/            	
        } catch (org.json.simple.parser.ParseException e) {
            e.printStackTrace();
            System.out.println(e.getMessage());
        }
	}
	
	
	/**
	 * session
	 */
	public Session getSession(){
		return this.session;
	}
	
	/**
	 * mess
	 */
	public void setMsg(String mess){
		this.msg = mess;
	}
	
	public String getMsg(){
		return this.msg;
	}
	
}
