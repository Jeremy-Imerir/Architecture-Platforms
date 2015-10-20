package Connect;

import java.io.IOException;
import java.util.ArrayList;

import org.codehaus.jackson.JsonParseException;
import org.codehaus.jackson.map.JsonMappingException;
import org.codehaus.jackson.map.ObjectMapper;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

import Map.Area;

public class ClientJSON {

	private String ip;
	private String port;
	
	/**
	 * Constructor without parameters
	 */
	public ClientJSON(){
		
	}
	
	/**
	 * Constructor with parameters
	 * @param ip
	 * @param port
	 */
	public ClientJSON(String ip, String port){
		this.setIp(ip);
		this.setPort(port);
	}
	
	
	/**
	 * Decode JSON send by HTTP
	 * @param message
	 */
	public String HTTP_JSON(String message){
		
		/* creating objects and JSONParser */
        JSONParser parser = new JSONParser();
        JSONObject jsonObject = null;
        
        String msg = null;
        
        ObjectMapper mapperClient = new ObjectMapper();
        
        try {
	    	jsonObject = (JSONObject) parser.parse(message);

	    	this.setIp(jsonObject.get("IP").toString());
	    	this.setPort(jsonObject.get("port").toString());
	    	msg = "ws://"+ getIp() + ":" + getPort() ;
	        
        } catch (org.json.simple.parser.ParseException e) {
            e.printStackTrace();
            System.out.println(e.getMessage());
        }
        return msg;
	}
	
	
	/**
	 * Decode JSON send by WebSocket
	 * @param message
	 */
	public void webSocketJSON(String message){
		
		/* creating objects and JSONParser JsonObject */
        JSONParser parser = new JSONParser();
        JSONObject jsonObject = null;
        
        ObjectMapper mapper = new ObjectMapper();
        
        try {
	    	jsonObject = (JSONObject) parser.parse(message);

	    	/* creation of new areas */
	        for (JSONObject o: (ArrayList<JSONObject>) jsonObject.get("areas")){

		    	Area area = mapper.readValue(o.toString(),Area.class);
		    	System.out.println("Le nom de l'area est: " + area.getName() + 
		    			" + taille de la fenetre-> w: " + area.getMap().getWeight().getW() + 
		    			", h: " + area.getMap().getWeight().getH());
		    	
	        }
	        
        } catch (org.json.simple.parser.ParseException e) {
            e.printStackTrace();
            System.out.println(e.getMessage());
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


	public String getIp() {
		return ip;
	}
	
	
	public void setIp(String ip) {
		this.ip = ip;
	}
	
	
	public String getPort() {
		return port;
	}
	
	
	public void setPort(String port) {
		this.port = port;
	}
}
