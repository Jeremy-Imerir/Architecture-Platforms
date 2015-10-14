import java.io.IOException;
import java.util.ArrayList;
import java.util.Collection;
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
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

@WebSocket(maxTextMessageSize = 64 * 1024)
public class ClientSocket extends Observable{

	private Session session;
	private String msg;
	CountDownLatch latch = new CountDownLatch(100);
	
	/* Socket message recu */
	@OnWebSocketMessage
	public void onMessage(String message) throws IOException{
		System.out.println("Message received from server: " + message);
		this.msg = message;
		
		/**
		 * JSON
		 */
		/* création des objets JSONObject et JSONParser */
        JSONParser parser = new JSONParser();
        JSONObject jsonObject = null;
        int nbQuartiers = 0;
        try {
        	jsonObject = (JSONObject) parser.parse(message);

//            /* création d'une liste d'objet JSON contenant les paramètres de la trame JSON ("dessin") */
            ArrayList<JSONObject> liste = (ArrayList<JSONObject>) jsonObject.get("areas");
            System.out.println("liste: " + liste + "\n");
            for(JSONObject a: liste){
//                /* on "isole" le contenu des objets dans une collection */
                Collection names = a.values();
                System.out.println("names: " + names + "\n");
//                /* pour tous les objets de la collection */ 
                for(Object obj: names) {
                	ArrayList<JSONObject> nom = (ArrayList<JSONObject>) obj;
                	for(JSONObject quartier: nom) {
                		Iterator it = nom.iterator();
                		Set set = quartier.keySet();
                		
                		// pour toutes les itérations
                        for (Iterator i = set.iterator(); i.hasNext();) {
                        	
                        }
                    }
                }
            }
        } catch (org.json.simple.parser.ParseException e) {
            e.printStackTrace();
            System.out.println(e.getMessage());
        }
        
        
		setChanged();
		notifyObservers(message);
	}
	
	/* Socket connect */
	@OnWebSocketConnect
	public void onConnect(Session session){
		System.out.println("Connected to server: ");
		this.session = session;
		sendMessage("{\"cmd\":\"areas\"}");
		//latch.countDown();
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
