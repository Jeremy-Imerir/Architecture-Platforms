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
	private int width;
	private int height;
	private PaintVertices paintVertices;
	private PaintStreets paintStreets;
	
	public Paint(){
		
	}
	
	public Paint(Area area, int width, int height){
		this.setA(area);
		this.setWidth(width);
		this.setHeight(height);
	}
	
	public void paintComponent(Graphics g){

        addMouseListener(this);
		super.paintComponent(g);
        Graphics2D graph2d = (Graphics2D) g.create();
        graph2d.setColor(Color.blue);
        
        paintVertices = new PaintVertices(this.a, graph2d, getWidth(), getHeight());
        paintStreets = new PaintStreets(this.a, graph2d);
        graph2d.dispose();   
	}
	

	/**
	 * Event MouseClicked
	 */
	@Override
	public void mouseClicked(MouseEvent e) {
		int mouseCursorX;
		int mouseCursorY;
		
		/* left mouse click */ 
		if(e.getButton() == MouseEvent.BUTTON3){
			mouseCursorX = e.getX();
			mouseCursorY = e.getY();
			
			System.out.printf("Position of mouse -> x: %d, y: %d \n", mouseCursorX, mouseCursorY);
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

	public Area getA() {
		return a;
	}

	public void setA(Area a) {
		this.a = a;
	}

	public int getWidth() {
		return width;
	}

	public void setWidth(int width) {
		this.width = width;
	}

	public int getHeight() {
		return height;
	}

	public void setHeight(int height) {
		this.height = height;
	}

	public PaintVertices getPaintVertices() {
		return paintVertices;
	}

	public void setPaintVertices(PaintVertices paintVertices) {
		this.paintVertices = paintVertices;
	}

	public PaintStreets getPaintStreets() {
		return paintStreets;
	}

	public void setPaintStreets(PaintStreets paintStreets) {
		this.paintStreets = paintStreets;
	}
}
