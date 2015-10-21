package Map;

public class Bridge {

	private String from;
	private ClassTo to;
	private float weight;
	
	/**
	 * Construtor without parameters
	 */
	public Bridge(){
		
	}
	
	/**
	 * Constructor with 3 parameters
	 * @param from
	 * @param t
	 * @param Weight
	 */
	public Bridge(String from, ClassTo t, float weight){
		this.setFrom(from);
		this.setTo(t);
		this.setWeight(weight);
	}


	public String getFrom() {
		return from;
	}


	public void setFrom(String from) {
		this.from = from;
	}


	public ClassTo getTo() {
		return to;
	}


	public void setTo(ClassTo to) {
		this.to = to;
	}
	public float getWeight() {
		return weight;
	}
	
	@Override
	public String toString() {
		return "Bridge [from=" + from + ", to=" + to + ", Weight=" + weight + "]";
	}
	public void setWeight(float weight) {
		this.weight = weight;
	}
}
