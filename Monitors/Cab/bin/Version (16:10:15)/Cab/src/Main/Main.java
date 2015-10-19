package Main;


import java.io.File;

import Connect.ClientSocket;
import Connect.Connect;


public class Main {

	/* main */
	public static void main(String[] args) {
//		/* create IHM */
//		IHM map = new IHM();
//		/* Resizes the map according to the size of the elements it contains */
//		map.pack();
//		/* center the window on the screen */
//		map.setLocationRelativeTo(null);
//		/* display */
//		map.setVisible(true);
		
		/**
		 *  connexion 
		 */
		Connect connection = new Connect();
		connection.start();
		
//		ClientSocket t = new ClientSocket();
//		t.testMapper(new File("/Users/matthieu/Desktop/IP_PORT.json"));
		
	}
}
