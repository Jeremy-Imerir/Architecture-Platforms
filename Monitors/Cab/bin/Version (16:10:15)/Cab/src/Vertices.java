
public class Vertices {
	
	private String name;
	private double x;
	private double y;
	
	/* constructor vertices */
	public Vertices(String name, double x, double y){
		this.setName(name);
		this.setX(x);
		this.setY(y);	
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
	 * GET VARIABLE X
	 * @return x
	 */
	public double getX() {
		return x;
	}

	/**
	 * SET VARIABLE X
	 * @param x
	 */
	public void setX(double x) {
		this.x = x;
	}

	/**
	 * GET VARIABLE Y
	 * @return y
	 */
	public double getY() {
		return y;
	}

	/**
	 * SET VARIABLE Y
	 * @param y
	 */
	public void setY(double y) {
		this.y = y;
	}
}
