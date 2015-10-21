package Map;

import java.util.ArrayList;

public class Map {

	private Weight weight;
	private ArrayList<Vertex> vertices;
	private ArrayList<Streets> streets;
	private ArrayList<Bridge> bridges;
	
	/**
	 * Constructor without parameters
	 */
	public Map(){
		
	}
	
	/**
	 * Constructor with 4 parameters
	 * @param w
	 * @param vertex
	 * @param streets
	 * @param bridge
	 */
	public Map(Weight w, ArrayList<Vertex> vertex, ArrayList<Streets> streets, ArrayList<Bridge> bridge){
		
		this.setVertices(vertex);
		this.setStreets(streets);
		this.setBridges(bridge);
	}


	@Override
	public String toString() {
		return "Map [Weight=" + weight + ", vertices=" + vertices + ", streets=" + streets + ", bridges=" + bridges
				+ "]";
	}

	/**
	 * Get weight
	 * @return
	 */
	public Weight getWeight() {
		return weight;
	}

	/**
	 * Set weight
	 * @param weight
	 */
	public void setWeight(Weight weight) {
		this.weight = weight;
	}
	
	
	/**
	 * Get Arraylist of verticex
	 * @return
	 */
	public ArrayList<Vertex> getVertices() {
		return vertices;
	}

	public void setVertices(ArrayList<Vertex> vertices) {
		this.vertices = vertices;
	}

	/**
	 * Get Arraylist of streets
	 * @return
	 */
	public ArrayList<Streets> getStreets() {
		return streets;
	}

	public void setStreets(ArrayList<Streets> streets) {
		this.streets = streets;
	}

	/**
	 * Get Arraylist of bridges
	 * @return
	 */
	public ArrayList<Bridge> getBridges() {
		return bridges;
	}

	public void setBridges(ArrayList<Bridge> bridges) {
		this.bridges = bridges;
	}


}
