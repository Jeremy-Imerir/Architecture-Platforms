package Cab;

public class CabRequest {

	private String area;
	private locVertex location;
	
	public CabRequest(){
		area = "";
		location = new locVertex();
	}

	public String getArea() {
		return area;
	}

	public void setArea(String area) {
		this.area = area;
	}
}
