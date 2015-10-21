package Cab;

public class CabRequest {

	private String area;
	private String from;
	private String to;
	
	public CabRequest(){
		area = "";
		from = "";
		to = "";
	}

	public String getArea() {
		return area;
	}

	public void setArea(String area) {
		this.area = area;
	}

	public String getFrom() {
		return from;
	}

	public void setFrom(String from) {
		this.from = from;
	}

	public String getTo() {
		return to;
	}

	public void setTo(String to) {
		this.to = to;
	}
}
