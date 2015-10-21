package Ihm;

import java.awt.Graphics2D;

import Map.Area;
import Map.Streets;
import Map.Vertex;

public class PaintStreets {

	
	public PaintStreets(){
		
	}
	
	public PaintStreets(Area area, Graphics2D graph){
		int x1 = 0;
		int x2 = 0;
		int y1 = 0;
		int y2 = 0;
		
		/*  */
		for(Streets object : area.getMap().getStreets()){
			String point1 = object.getPath().get(0);
			String point2 = object.getPath().get(1);
			
			/*  */
			for(Vertex objVertex : area.getMap().getVertices()){
				if(objVertex.getName() == point1){
					x1 = (int)objVertex.getX();
					y1 = (int)objVertex.getY();
				}
				if(objVertex.getName() == point2){
					x2 = (int)objVertex.getX();
					y2 = (int)objVertex.getY();
				}
			}
			
			graph.drawLine(x1, y1, x2, y2);
			
		}
	}
}
