package Ihm;

import java.awt.Dimension;

import javax.swing.JFrame;
import javax.swing.JPanel;

import Map.Area;

public class Frames extends JFrame {

	private Paint paint;
	private int width = 400;
	private int height = 400;
	
	public Frames(Area a){
		
		/* get fenetre size */
		Dimension size = java.awt.Toolkit.getDefaultToolkit().getScreenSize();
		this.width = (int)size.getWidth();
		this.height = (int) size.getHeight();
		
		JFrame frame = new JFrame("Cab " + a.getName());
		
		paint = new Paint(a, this.width, this.height);
		
		/* add paint in frame*/
		frame.add(paint);

		frame.setSize(this.width, this.height);
		frame.setResizable(false);
		frame.setVisible(true);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
}
