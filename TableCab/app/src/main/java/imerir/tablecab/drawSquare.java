package imerir.tablecab;

/**
 * Created by Brice-PC on 21/10/2015.
 */
import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.Paint.Style;
import android.util.AttributeSet;
import android.view.View;

public class drawSquare extends View{
    Paint paint=new Paint();

    public drawSquare(Context context) {
        super(context);
        paint.setColor(Color.RED);
        paint.setStyle(Style.STROKE);

    }
    //Rect rec =new Rect();
    public drawSquare(Context con,AttributeSet atts)
    {
        super(con, atts);

    }

    @Override
    public void onDraw(Canvas canvas) {
        canvas.drawLine(20,40,450,40,paint);          //horizontal top
        canvas.drawRect(70,140,400,500,paint);

        canvas.drawLine(20,40,20,500,paint);            //verticalleft
        canvas.drawLine(20,700,450,500,paint);   //horizontal bottom
        canvas.drawLine(450, 40, 450, 500, paint);   //vertical right
    }
}
