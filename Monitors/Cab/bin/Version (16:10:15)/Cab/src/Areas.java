import java.util.ArrayList;
import java.util.HashMap;

import org.json.simple.JSONObject;

public class Areas {

	private String name;
	private double w;
	private double h;
	private HashMap<String, Vertices> vertices;
	private HashMap<String, Streets> streets;
	
	/* constructor area */
	public Areas(JSONObject area){
		this.name = (String) area.get("name");
		this.w = Double.parseDouble(((JSONObject)((JSONObject)area.get("map")).get("weight")).get("w").toString());
		this.h = Double.parseDouble(((JSONObject)((JSONObject)area.get("map")).get("weight")).get("h").toString());
		createVertices(((ArrayList<JSONObject>)((JSONObject)area.get("map")).get("vertices")));
	}
	
	/* create vertices of JSON */
	public void createVertices(ArrayList<JSONObject> vertice){
		this.vertices = new HashMap<>();
		for(JSONObject o: vertice){
			String name = (String)o.get("name");
			double x = Double.parseDouble(o.get("x").toString());
			double y = Double.parseDouble(o.get("y").toString());
			this.vertices.put(name, new Vertices(name,x,y));
		}
	}
	
	/* create streets of JSON */
	public void createStreets(ArrayList<JSONObject> street){
		this.streets = new HashMap<>();
		for(JSONObject o: street){
			/* get the name, the oneway */
			String name = (String)o.get("name");
			boolean oneway = (boolean)o.get("oneway");
			
			ArrayList<Vertices> path = new ArrayList();
			for(String point: ((ArrayList<String>)o.get("path"))){
				path.add(getVerticeName(name));
				this.streets.put(name, new Streets(name,path,oneway));
			}
		}
	}
	
	/* get vertice by passing name */
	public Vertices getVerticeName(String name){
		return this.vertices.get(name);
	}
}
