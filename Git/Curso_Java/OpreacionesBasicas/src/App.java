package OpreacionesBasicas.src;

import java.util.Scanner;

public class App {
    public static void main(String[] args){
        Operaciones op =new Operaciones();
     Scanner a = new Scanner(System.in);
     double num1, num2;
     System.out.println("Ingresa el primer numero");
     num1= a.nextDouble();
     System.out.println("Ingresa el segundo numero");
     num2= a.nextDouble();
    
op.Resultado(num1, num2);
    }
}
