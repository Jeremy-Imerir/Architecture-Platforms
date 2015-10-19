package Map;

public class Vertex {

	private String name;
	private double x;
	private double y;
	
	
	public Vertex(){
		
	}
		
	public Vertex(String name, double x, double y){
		this.setName(name);
		this.setX(x);
		this.setY(y);
	}

	@Override
	public String toString() {
		return "Vertex [name=" + name + ", x=" + x + ", y=" + y + "]";
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public double getX() {
		return x;
	}

	public void setX(double x) {
		this.x = x;
	}

	public double getY() {
		return y;
	}

	public void setY(double y) {
		this.y = y;
	}
}
