import java.util.ArrayList;

public class Streets {

	/* declaration of variables */
	private String name;
	private ArrayList<Vertices> path;
	private boolean oneway; 
	
	/* constructor streets */
	public Streets(String n, ArrayList<Vertices> list, boolean b){
		this.setName(n);
		this.setPath(list);
		this.setOneway(b);
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
	 * GET PATH
	 * @return path
	 */
	public ArrayList<Vertices> getPath() {
		return path;
	}

	/**
	 * SET PATH
	 * @param path
	 */
	public void setPath(ArrayList<Vertices> path) {
		this.path = path;
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
}
