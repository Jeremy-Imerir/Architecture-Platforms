package Ihm;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.geom.Rectangle2D;

import javax.swing.JFrame;
import javax.swing.JPanel;

import Map.Area;
import Map.Vertex;

public class Paint extends JPanel implements MouseListener{
	
	/* declaration of variables */
	private Area a;
	private float weight;
	private float height;
	private PaintVertices paintVertices;
	private PaintStreets paintStreets;
	
	public Paint(){
		
	}
	
	public Paint(Area area, int weight, int height){
		this.a = area;
		this.weight = weight;
		this.height = height;
	}
	
	public void paintComponent(Graphics g){
		
		super.paintComponent(g);
        Graphics2D graph2d = (Graphics2D) g.create();
        graph2d.setColor(Color.blue);
        
        paintVertices = new PaintVertices(this.a, graph2d, this.weight, this.height);
        
        graph2d.dispose();
        
        addMouseListener(this);
	}
	

	/**
	 * Event MouseClicked
	 */
	@Override
	public void mouseClicked(MouseEvent e) {
		float mouseCursorX;
		float mouseCursorY;
		
		/* left mouse click */ 
		if(e.getButton() == MouseEvent.BUTTON1){
			mouseCursorX = e.getX();
			mouseCursorY = e.getY();
			
			System.out.println("Position of x: " + mouseCursorX);
			System.out.println("Position of x: " + mouseCursorY);
		}
	}

	@Override
	public void mousePressed(MouseEvent e) {
		// TODO Auto-generated method stub
	}

	@Override
	public void mouseReleased(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void mouseEntered(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void mouseExited(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}
}
