package Ihm;

import javax.swing.JFrame;
import javax.swing.JPanel;

import Map.Area;

public class Frames extends JFrame {

	private Paint paint;
	private float weight = 400.0f;
	private float height = 400.0f;
	
	public Frames(Area a){
		JFrame frame = new JFrame("Cab " + a.getName());
		//frame.setSize(weight, height);
		frame.setExtendedState(JFrame.MAXIMIZED_BOTH);
		frame.setResizable(false);
		frame.setVisible(true);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		paint = new Paint(a, frame.getWidth(), frame.getHeight());
		JPanel pan = new JPanel();
		frame.add(pan);
		pan.add(paint);
	}
}
