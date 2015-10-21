package Map;


import java.util.ArrayList;

public class Streets {

	/* declaration of variables */
	private String name;
	private ArrayList<String> path;
	private boolean oneway; 
	
	public Streets(){
		
	}
	
	/* constructor streets */
	public Streets(String name, ArrayList<String> path, boolean b){
		this.setName(name);
		this.setPath(path);
		this.setOneway(b);
	}

	@Override
	public String toString() {
		return "Streets [name=" + name + ", path=" + path + ", oneway=" + oneway + "]";
	}

	/**
	 * GET NAME
	 * @return name
	 */
	public String getName() {
		return name;
	}

	/**
	 * SET NAME
	 * @param name
	 */
	public void setName(String name) {
		this.name = name;
	}

	/**
	 * GET ONEWAY
	 * @return oneway
	 */
	public boolean isOneway() {
		return oneway;
	}

	/**
	 * SET ONEWAY
	 * @param oneway
	 */
	public void setOneway(boolean oneway) {
		this.oneway = oneway;
	}

	public ArrayList<String> getPath() {
		return path;
	}

	public void setPath(ArrayList<String> path) {
		this.path = path;
	}

}
