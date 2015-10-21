package Connect;


import java.io.IOException;

import org.eclipse.jetty.websocket.api.Session;
import org.eclipse.jetty.websocket.api.annotations.OnWebSocketClose;
import org.eclipse.jetty.websocket.api.annotations.OnWebSocketConnect;
import org.eclipse.jetty.websocket.api.annotations.OnWebSocketMessage;
import org.eclipse.jetty.websocket.api.annotations.WebSocket;

@WebSocket(maxTextMessageSize = 64 * 1024)
public class ClientSocket{

	private Session session;
	private String msg;
	private ClientJSON client = new ClientJSON();
	
	/**
	 * socket message received
	 * @param message
	 * @throws IOException
	 */
	@OnWebSocketMessage
	public void onMessage(String message) throws IOException{
		this.msg = message;
		
		/* reads and interprets the JSON */
        client.webSocketJSON(message);        
	}
	
	/**
	 * socket connect
	 * @param session
	 */
	@OnWebSocketConnect
	public void onConnect(Session session){
		System.out.println("Connected to server: ");
		this.session = session;
	}

	/**
	 * socket message sent
	 * @param str
	 */
	public void sendMessage(String str){
		try {
			session.getRemote().sendString(str);
		} catch (IOException e){
			e.printStackTrace();
		}
	}
	
	
	/**
	 * socket close
	 * @param statusCode
	 * @param reason
	 */
	@OnWebSocketClose
	public void onClose(int statusCode, String reason) {
        System.out.printf("Connection closed: %d - %s%n", statusCode, reason);
        this.session = null;
    }
	
	
	/**
	 * get session
	 */
	public Session getSession(){
		return this.session;
	}
	
	/**
	 * get and set mess
	 */
	public void setMsg(String mess){
		this.msg = mess;
	}
	
	public String getMsg(){
		return this.msg;
	}
	
}
