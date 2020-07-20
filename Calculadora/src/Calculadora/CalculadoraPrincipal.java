package Calculadora;
import java.util.Scanner;
public class CalculadoraPrincipal {

	public static void main(String[] args) {
		Scanner teclado =new Scanner(System.in);
		double resultadosuma = 0;
		double resultadoresta = 0;
		double resultadomultiplicacion = 0;
		double resultadoDivision=0;
		double resultadoResto=0;
		double num1,num2;
		System.out.println("Introduce los dos numeros a realizar");
		num1=Double.parseDouble(teclado.nextLine());
		num2=Double.parseDouble(teclado.nextLine());
		teclado.close();
		System.out.println("La suma da: "+Suma(resultadosuma, num1, num2));
		System.out.println("La resta da: "+Resta(resultadoresta, num1, num2));
		System.out.println("La multiplicacion da: "+Multiplicacion(resultadomultiplicacion, num1, num2));
		System.out.println("La division da: "+DivisionConsciente(resultadoDivision, num1, num2));
		System.out.println("El resto es: "+DivisionResto(resultadoResto, num1, num2));
}
	private static double Suma (double resultadosuma,double num1,double num2) {
		double resultado;
		resultado=num1+num2;
		resultadosuma=resultado;
		return resultado;
	}
	private static double Resta (double resultadoresta,double num1,double num2) {
		double resultado;
		resultado=num1-num2;
		resultadoresta=resultado;
		return resultado;
	}
	private static double Multiplicacion (double resultadomultiplicacion,double num1,double num2) {
		double resultado;
		resultado=num1*num2;
		resultadomultiplicacion=resultado;
		return resultado;
	}
	private static double DivisionConsciente (double resultadoDivision,double num1,double num2) {
		double resultado;
		resultado=num1/num2;
		resultadoDivision=resultado;
		return resultado;
	}
	private static double DivisionResto (double resultadoResto,double num1,double num2) {
		double resultado;
		resultado=num1%num2;
		resultadoResto=resultado;
		return resultado;
	}
}
