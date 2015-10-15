package Carte;
import java.awt.Dimension;
import java.awt.Graphics;

import javax.swing.JFrame;
import javax.swing.JPanel;

public class IHM extends JFrame implements Constantes{

	private Modele modele;
	public IHM(){
	
		/* titre de la fenêtre */
		super("Interface");
		/* création du modèle */
		this.modele = new Modele();
		/* ferme l'application lorsque la fenêtre est fermée */
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		/* fenetre non redimensionnable */
		setResizable(false);
		
		/* panel qui affichera le jeu */
		final JPanel jeu = new JPanel(){
			@Override
	        protected void paintComponent(Graphics g) {
	              super.paintComponent(g);
	              // affichage du modèle du jeu
	              IHM.this.modele.affichage(g);
			}
        };
        
		/* dimension du panel */
		//jeu.setPreferredSize(new Dimension(NB_COLONNES * CASE_EN_PIXELS, NB_LIGNES * CASE_EN_PIXELS));
		jeu.setPreferredSize(new Dimension(300,300));
		
		/* ajout du panel à la fenêtre */
		setContentPane(jeu);
		
		/* création d'un thread infini */
		Thread thread = new Thread(new Runnable() {
			
			@Override
			public void run() {
				/* boucle infini */
				while (true){
					IHM.this.modele.calcul();
					
					/* redessine le jeu */
					jeu.repaint();
					
					/* temps d'attente pour l'oeil humain */
					try {
                        Thread.sleep(500);
					} catch (InterruptedException e) {
						
					}
				}
			}
		});
		/* lancement du thread */
		thread.start();
	}
	
}
