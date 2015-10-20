package Map;



public class ClassTo {
	private String area;
	private String vertex;
	
	public ClassTo(){
		
	}
	
	public ClassTo(String area, String vertex){
		this.setArea(area);
		this.setVertex(vertex);
	}


	@Override
	public String toString() {
		return "ClassTo [area=" + area + ", vertex=" + vertex + "]";
	}

	public String getArea() {
		return area;
	}

	
	public void setArea(String area) {
		this.area = area;
	}


	public String getVertex() {
		return vertex;
	}


	public void setVertex(String vertex) {
		this.vertex = vertex;
	}
}
