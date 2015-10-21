package Cab;

public class CabInfo {

	private float odometer;
	private CabRequest request;
	private locVertex loc_now;
	private locVertex loc_prior;
	
	public CabInfo(){
		odometer = 0;
		request = new CabRequest();
		loc_now = new locVertex();
		loc_prior = new locVertex();
	}

	public float getOdometer() {
		return odometer;
	}

	public void setOdometer(float odometer) {
		this.odometer = odometer;
	}

	public CabRequest getRequest() {
		return request;
	}

	public void setRequest(CabRequest request) {
		this.request = request;
	}

	public locVertex getLoc_now() {
		return loc_now;
	}

	public void setLoc_now(locVertex loc_now) {
		this.loc_now = loc_now;
	}

	public locVertex getLoc_prior() {
		return loc_prior;
	}

	public void setLoc_prior(locVertex loc_prior) {
		this.loc_prior = loc_prior;
	}
	
	
}
