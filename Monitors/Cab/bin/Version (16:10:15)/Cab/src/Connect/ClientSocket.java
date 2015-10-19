package Connect;


import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Observable;

import org.codehaus.jackson.JsonParseException;
import org.codehaus.jackson.map.JsonMappingException;
import org.codehaus.jackson.map.ObjectMapper;

import org.eclipse.jetty.websocket.api.Session;
import org.eclipse.jetty.websocket.api.annotations.OnWebSocketConnect;
import org.eclipse.jetty.websocket.api.annotations.OnWebSocketMessage;
import org.eclipse.jetty.websocket.api.annotations.WebSocket;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

import Map.Area;

@WebSocket(maxTextMessageSize = 64 * 1024)
public class ClientSocket extends Observable{

	private Session session;
	private String msg;
	private ClientJSON client = new ClientJSON();
	
	/* socket message received */
	@OnWebSocketMessage
	public void onMessage(String message) throws IOException{
		System.out.println("Message received from server: " + message);
		this.msg = message;
		
		/* reads and interprets the JSON */
        client.webSocketJSON(message);
        
	}
	
	/* socket connect */
	@OnWebSocketConnect
	public void onConnect(Session session){
		System.out.println("Connected to server: ");
		this.session = session;
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
	
	
	/*****************************TEST JSON*****************************/
	public void testMapper(File file) {
		 ObjectMapper mapper = new ObjectMapper();
		 
		 try {
			ClientJSON test = mapper.readValue(file, ClientJSON.class);
			
//			System.out.println("Map: " + areas.getMap());
//			System.out.println("Le h du weight est: " + areas.getMap().getWeight().getH());
			
			
		} catch (JsonParseException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (JsonMappingException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
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
