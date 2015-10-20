package Connect;


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URI;
import java.net.URL;
import java.util.Observer;

import org.eclipse.jetty.websocket.client.WebSocketClient;
import org.json.simple.JSONObject;

public class Connect extends Thread {

	
	private String url = "http://172.30.0.227:8080";
	private WebSocketClient client = new WebSocketClient();
	private	ClientSocket socket = new ClientSocket();
	
	public void run(){
		try {
			/* get the HTTP address */
			String destinataire = getURL(url);

			/* decode JSON send by HTTP */
			ClientJSON httpJson = new ClientJSON();
			String address = httpJson.HTTP_JSON(destinataire);
			
			/* create the webSocket connection */
			client.start();
			URI echoURI = new URI(address);
			client.connect(socket, echoURI);
			
		}catch (Throwable t){
			t.printStackTrace();
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
