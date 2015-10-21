package Ihm;

import java.awt.Graphics2D;
import java.awt.geom.Rectangle2D;

import Map.Area;
import Map.Vertex;

public class PaintVertices {

	public PaintVertices(){
		
	}
	
	public PaintVertices(Area area, Graphics2D graph, float w, float h){
		for(Vertex object : area.getMap().getVertices()){
			float x = object.getX() * w;
			float y = object.getY() * h;
			
			Rectangle2D rect1 = new Rectangle2D.Double(x, y, 30.0, 30.0);
			Rectangle2D rect2 = new Rectangle2D.Double(x, y, 30.0, 30.0);
			graph.fill(rect1);
			graph.draw(rect2);
		}
	}
}
