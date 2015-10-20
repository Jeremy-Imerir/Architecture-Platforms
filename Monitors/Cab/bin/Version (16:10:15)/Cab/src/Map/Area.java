package Map;


public class Area {

	private String name;
	private Map map;
	
	/**
	 * Constructor without parameters
	 */
	public Area(){
		
	}
	
	/**
	 * Constructor with 2 parameters
	 * @param name
	 * @param map
	 */
	public Area(String name, Map m){
		this.setName(name);
		this.setMap(m);
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public Map getMap() {
		return map;
	}

	public void setMap(Map map) {
		this.map = map;
	}
}
