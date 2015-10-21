package Cab;

public class CabInfo {

	private float x;
	private float y;
	private float distanceToEnd;
	private String goTo;
	private String status;
	
	public CabInfo(){
		x = 0.0f;
		y = 0.0f;
		distanceToEnd = 0.0f;
		goTo = "";
		status = "";
	}

	public float getX() {
		return x;
	}

	public void setX(float x) {
		this.x = x;
	}

	public float getY() {
		return y;
	}

	public void setY(float y) {
		this.y = y;
	}

	public float getDistanceToEnd() {
		return distanceToEnd;
	}

	public void setDistanceToEnd(float distanceToEnd) {
		this.distanceToEnd = distanceToEnd;
	}

	public String getGoTo() {
		return goTo;
	}

	public void setGoTo(String goTo) {
		this.goTo = goTo;
	}

	public String getStatus() {
		return status;
	}

	public void setStatus(String status) {
		this.status = status;
	}
	
}
