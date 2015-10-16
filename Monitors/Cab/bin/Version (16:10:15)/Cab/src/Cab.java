import Carte.IHM;

public class Cab {

	/* main */
	public static void main(String[] args) {
		/* create IHM */
		IHM map = new IHM();
		/* Resizes the map according to the size of the elements it contains */
		map.pack();
		/* center the window on the screen */
		map.setLocationRelativeTo(null);
		/* display */
		map.setVisible(true);
		
		// connexion 
//		Connect connection = new Connect();
//		connection.run();
//		a b = new a();
//		connection.addObserver(b);
		
		
		
	}
}
