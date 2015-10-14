package Carte;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import java.util.LinkedList;

public class Chemin {

	/* liste  */
	private LinkedList<Case> chemin;
	
	/**
	 * CONSTRUCTEUR
	 */
	public Chemin(){
		this.chemin = new LinkedList<Case>();
		this.chemin.add(new Case((15),15));
//		this.chemin.add(new Case((16),15));
		this.chemin.add(new Case((17),15));
	}
	
	public void calcul(){
		/**
		 *  Calcul 
		 */
	}
	
	
	/* Affichage du chemin */
	public void affichage(Graphics g){
		
		/* Améliore l'aspect graphique */
		Graphics2D graphique2D = (Graphics2D) g;
		graphique2D.setRenderingHint(RenderingHints.KEY_ANTIALIASING,
									 RenderingHints.VALUE_ANTIALIAS_ON);
		
		/* itération des éléments de la collection */
		 for(Case c : this.chemin){
			 g.fillRect(c.getX(), c.getY(), c.getLargeur(), c.getHauteur());
			 //g.fillRect(c.getIndiceX(), c.getIndiceY(), c.getLargeur(), c.getHauteur());
		 }
		
	}
}
