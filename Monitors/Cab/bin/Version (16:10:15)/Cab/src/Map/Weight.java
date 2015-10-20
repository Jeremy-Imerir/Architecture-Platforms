package Map;

public class Weight {

	private float w;
	private float h;
	
	
	/**
	 * Constructor without parameters
	 */
	public Weight(){
		
	}
	
	/**
	 * Constructor with parameters
	 */
	public Weight(float w, float h){
		this.setW(w);
		this.setH(h);
	}

	/**
	 * Get w
	 * @return
	 */
	public float getW() {
		return w;
	}

	/**
	 * Set w
	 * @param w
	 */
	public void setW(float w) {
		this.w = w;
	}

	/**
	 * Get w
	 * @return
	 */
	public float getH() {
		return h;
	}

	/**
	 * Set w
	 * @param h
	 */
	public void setH(float h) {
		this.h = h;
	}
}
