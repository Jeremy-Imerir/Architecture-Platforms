package Carte;
public class Case implements Constantes{

	private int x;
	private int y;
	
	/**
	 * CONSTRUCTEUR
	 */
	public Case(int coordX, int coordY){
		this.x = coordX;
		this.y = coordY;
	}

	/**
	 * SETTER
	 */
	public void setX(int coordX){
		this.x = coordX;
	}
	
	public void setY(int coordY){
		this.y = coordY;
	}
	
	
	/**
	 * GETTER
	 */
	public int getIndiceX(){
		return this.x;
	}
	
	public int getIndiceY(){
		return this.y;
	}
	

	/**
	 * COORDONNEES EN PIXELS
	 */
    public int getX() {
          return this.x * CASE_EN_PIXELS;
    }

    public int getY() {
          return this.y * CASE_EN_PIXELS;
    }

    public int getLargeur() {
          return CASE_EN_PIXELS;
    }

    public int getHauteur() {
          return CASE_EN_PIXELS;
    }
}
