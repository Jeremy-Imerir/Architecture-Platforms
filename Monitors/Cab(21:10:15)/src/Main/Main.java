package Main;


import java.io.File;

import Connect.ClientSocket;
import Connect.Connect;


public class Main {

	/* main */
	public static void main(String[] args) {
		/**
		 *  connexion 
		 */
		Connect connection = new Connect();
		connection.start();
		
//		ClientSocket t = new ClientSocket();
//		t.testMapper(new File("/Users/matthieu/Desktop/Area.json"));
		
	}
}
