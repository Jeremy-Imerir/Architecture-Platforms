import Carte.IHM;

public class Cab {

	public static void main(String[] args) {
		/* création de la fenêtre */
		IHM map = new IHM();
		/* Redimensionne la map suivant la taille des éléments qu'elle contient */
		map.pack();
		/* centre la fenetre sur l'écran */
		map.setLocationRelativeTo(null);
		/* affichage */
		map.setVisible(true);
		
		// connexion 
//		Connect connection = new Connect();
//		connection.run();
//		a b = new a();
//		connection.addObserver(b);
		
		
		
	}
}
