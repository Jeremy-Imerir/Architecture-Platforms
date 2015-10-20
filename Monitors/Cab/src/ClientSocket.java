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
	CountDownLatch latch = new CountDownLatch(100);
	
	/* Declaration des variables */
	int nbQuartiers = 0;
    int w = 0;
    int h = 0;
    int tab[][] = null;
    HashMap <String, Areas> areas;
	
	/* Socket message recu */
	@OnWebSocketMessage
	public void onMessage(String message) throws IOException{
		System.out.println("Message received from server: " + message);
		this.msg = message;
		
		/* lit et interprete le JSON */
        readJSON(message);
        
//		setChanged();
//		notifyObservers(message);
	}
	
	/* Socket connect */
	@OnWebSocketConnect
	public void onConnect(Session session){
		System.out.println("Connected to server: ");
		this.session = session;
		//sendMessage("{\"cmd\":\"areas\"}");
	}

	/* Socket message envoyé */
	public void sendMessage(String str){
		try {
			session.getRemote().sendString(str);
		} catch (IOException e){
			e.printStackTrace();
		}
	}
	

	/* Garde la connexion ouverte */
	public boolean awaitClose(int i, TimeUnit hours) throws InterruptedException{
		return this.latch.await(i, hours);
	}
	
	/* Socket close */
	@OnWebSocketClose
	public void onClose(int statusCode, String reason) {
        System.out.printf("Connection closed: %d - %s%n", statusCode, reason);
        this.session = null;
        this.latch.countDown();
    }
	
	/**
	 * JSON
	 */
	public void readJSON(String message){
		/* création des objets JSONObject et JSONParser */
        JSONParser parser = new JSONParser();
        JSONObject jsonObject = null;
        try {
	    	jsonObject = (JSONObject) parser.parse(message);
	        
	    	/* Creation d'une nouvelle areas */
//	    	this.areas = new HashMap<String, Areas>();
//	        for (JSONObject o: (ArrayList<JSONObject>) jsonObject.get("areas")){
//	        	this.areas.put((String)o.get("name"), new Areas());
//	        }
	        
	        
	        /* création d'une liste d'objet JSON contenant les paramètres de la trame JSON ("areas") */
	        JSONArray areas = (JSONArray) jsonObject.get("areas");
	    	Iterator ite_areas = areas.iterator();
            
		    /* Name */
            while (ite_areas.hasNext()) {
                JSONObject obj1 = (JSONObject) ite_areas.next();
                /* Map */
                JSONObject map = (JSONObject) obj1.get("map");
                System.out.println(map);
                /* Weight */
                JSONObject weight = (JSONObject) map.get("weight");
                
                /* Obtient les valeurs de w et h */
                Collection col_weight = weight.values();
                Iterator i = col_weight.iterator();
                System.out.println(i.next());
                
                
//                for( Object obj: col_weight) {
//                    /* création d'une liste d'objets JSON contenant les objets de la collection */
//                    ArrayList<JSONObject> keyl = (ArrayList<JSONObject>) obj;
////                    System.out.println(keyl.get(0));
//                }
                /* Vertices */
                JSONArray vertices = (JSONArray) map.get("vertices");
//                System.out.println(vertices);
//                Iterator ite_vertices = vertices.iterator();
//                JSONObject obj2 = (JSONObject) ite_vertices.next();
//                
//                /* recupere le X et le Y des differents points */
//                for(int i=0 ;i<vertices.size() ;i++){
//                	for(int j=0; j<vertices.size();j++){
//                		tab[i][j] = (double) obj2.get("x");
//                		j++;
//                		tab[i][j] = (double) obj2.get("y");
//                	}
//                }
                
                /* Streets */
//                JSONArray streets = (JSONArray) jsonObject.get("streets");
//                Iterator ite_streets = streets.iterator();
//                /* Bridges */
//                JSONArray bridges = (JSONArray) jsonObject.get("bridges");
//                Iterator ite_bridges = bridges.iterator();
                
                
                
                /* Weight, Vertices, Streets and Bridges */
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
//	            /* on "isole" le contenu des objets dans une collection */
//	          	Collection names = a.values();
//			    System.out.println("names: " + names + "\n");
//			    // get an array from the JSON object
//			                
//	        }
//            System.out.println("liste: " + liste + "\n");
//            for(JSONObject a: liste){
//                /* on "isole" le contenu des objets dans une collection */
//            	Collection names = a.values();
//                System.out.println("names: " + names + "\n");
//                /* pour tous les objets de la collection */
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
	
	public CountDownLatch getLatch(){
		return latch;
	}
}
