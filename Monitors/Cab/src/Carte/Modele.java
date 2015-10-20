package Carte;
import java.awt.Graphics;

public class Modele {

	private Chemin chemin;
	
	/**
	 * CONSTRUCTEUR
	 */
	public Modele(){
		this.chemin = new Chemin();
	}
	
	/* les calculs du jeu */
	public void calcul(){
		/* calcul du chemin */
		this.chemin.calcul();;
	}
	
	/* le graphique du jeu */
	public void affichage(Graphics g){
		/* affichage du chemin */
		this.chemin.affichage(g);		
	}
}
