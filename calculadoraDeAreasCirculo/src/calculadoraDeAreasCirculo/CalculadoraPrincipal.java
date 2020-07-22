package calculadoraDeAreasCirculo;
import java.util.Scanner;
public class CalculadoraPrincipal {
/**
 * 
 * @author xXxArroyoxXx
 */
	public static void main(String[] args) {
		Scanner teclado=new Scanner(System.in);
		double radio,area;
		area=0;
		System.out.println("Cual es el radio de tu circulo?");
		radio=Double.parseDouble(teclado.nextLine());
		teclado.close();
		System.out.println("El area es de :"+Area(area,radio));
	}
	public static double Area (double area,double radio) {
		area=Math.PI*Math.pow(radio, 2);
	return area;
	}

}
