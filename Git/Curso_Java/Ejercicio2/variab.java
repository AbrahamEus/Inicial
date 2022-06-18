package Ejercicio2;

import java.util.Scanner;
public class variab {
public static void main(String[] args) {
  Scanner sc= new Scanner(System.in);
  int lado;

  System.out.println("Calculando el area y perimetro del cuadrado");
  System.out.println("Introduce el lado del cuadrado");
  lado= sc.nextInt();

  int area,perimetro;
  area= lado*lado;
  perimetro= lado+lado+lado+lado;

  System.out.println("Area del cuadrado: \n"+area);
  System.out.println("Perimetro del cuadrado: \n"+perimetro);
  
}
}