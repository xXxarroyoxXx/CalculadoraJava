package conversorASCII;
import java.util.Scanner;
public class ConversorPrincipal {
	public static void main(String[] args) {
		/*
		 * author xXxArroyoxXx
		 * 
		 */
		Scanner teclado=new Scanner(System.in);
		int eleccion;
		do {
		System.out.println("Pulse 1.ASCII-CHAR\n"
				+ "2.CHAR-ASCII\n"
				+ "3.Salir");
		eleccion=Integer.parseInt(teclado.nextLine());
		switch (eleccion){
			case 1:
				char caracter;
				System.out.println("Introduzca el caracter deseado");
				caracter=teclado.next().charAt(0);
				int ascii=(int)caracter;
				System.out.println("El codigo ASCII es:"+ascii);
				break;
			case 2:
				int numASCII;
				System.out.println("Introduce el codigo ASCII deseado");
				numASCII=Integer.parseInt(teclado.nextLine());
				char c=(char)numASCII;  
				System.out.println(c);  
				break;
			default:
				break;
			}
		}while (eleccion!=3);
		teclado.close();
	}
}
//.y hago otra calculadora
