import org.json.simple.JSONObject;

public class Areas {

	private String name;
	private double w;
	private double h;
	
	public Areas(JSONObject area){
		this.name = (String) area.get("name");
		this.w = (double) area.get("w");
	}
}
