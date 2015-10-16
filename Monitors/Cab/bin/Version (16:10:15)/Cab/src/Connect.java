import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URI;
import java.net.URL;
import java.util.Observer;
import java.util.concurrent.TimeUnit;

import org.eclipse.jetty.websocket.client.WebSocketClient;

public class Connect extends Thread {

//	private String dest = "ws://172.30.0.184:2009";
//	private String URL = "http://172.30.0.184:80/deviceConnect";
//	private String dest = "ws://172.30.0.170:8000";
	private String url = "http://172.30.0.170:8080";
	private WebSocketClient client = new WebSocketClient();
	private	ClientSocket socket = new ClientSocket();
	
	public void run(){
		try {
			client.start();
			
			/* get the HTTP address */
			String destinataire = getURL(url);
			System.out.println(destinataire);
			
			URI echoURI = new URI(destinataire);
			client.connect(socket, echoURI);
			
		}catch (Throwable t){
			t.printStackTrace();
		}finally {
			try {
				client.stop();
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
	}
	
	/**
	 *  HTTP GET REQUEST
	 */
	public String getURL(String url) throws Exception{
		/* variables */
		URL obj = new URL(url);
		HttpURLConnection con = (HttpURLConnection) obj.openConnection();
		String inputLine;
		StringBuffer response = new StringBuffer();
		String message_recu = null;
		
		/* GET request */
		con.setRequestMethod("GET");

		int responseCode = con.getResponseCode();
		System.out.println("\nSending 'GET' request to URL : " + url);

		BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));

		while ((inputLine = in.readLine()) != null) {
			response.append(inputLine);
		}
		in.close();

		message_recu = response.toString();
		
		return message_recu;
	}
	
//	
//	/**
//	 * set &  receiver
//	 */
//	public void setDest(String dest){
//		this.dest = dest;
//	}
//	
//	public String getDest(){
//		return this.dest;
//	}
	
	/**
	 * return client
	 */
	public WebSocketClient getSocketClient(){
		return this.client;
	}
	
	/**
	 * socket
	 */
	public ClientSocket getClientSocket(){
		return this.socket;
	}

	public void addObserver(Observer b) {
		this.socket.addObserver(b);
	}
}
