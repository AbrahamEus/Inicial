package OpreacionesBasicas.src;

public class Operaciones {
    public static double Suma(Double a, Double a1){
        return a+a1;
    }
    public double Resta(Double a, Double a1){
        return a-a1;
    }
    public double Multiplicacion(Double a, Double a1){
        return a*a1;
    }
    public double Division(Double a, Double a1){
        return a/a1;
    }
    
    public void Resultado(Double a,Double a1){
        System.out.println("El resultado de la Suma es: "+Suma(a, a1)+"\nEl resultado de la Resta es: "+Resta(a, a1)+
        "\nEl resultado de la Multiplicacion es: "+Multiplicacion(a, a1)+"\nEl resultado de la Division es: "+Division(a,a1));
    }
}
