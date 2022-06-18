"""
¿Que es un condicional ?

Un acción <<condicional>> es aquella que se realiza si se presenta una condición

Los condicionales están en nuestra vida diaria. Ejemplos:
* Si hay previsión de lluvia, entonces voy a coger un paraguas.
*Si he suspendido el examen , entonces debo estudiar más.
*Si tengo sed, entonces debo beber.

En programación, una <<expresión condicional>> es esencialmente lo mismo

<<TIPOS DE CONDICIONES>>
#La condicion debe de ser:
 *Un valor booleano (True o False).
 *Una expresión que devuelva un valor booleano(por ejemplo, una expresión relacional ).
 *La combinacion de valores booleanos mediante operadores booleanos (AND,OR,NOT)
La condicion se cumple cuando el valor evaluado es <<true>. Por ejemplo:

if True:  #Siempre se cumple
if False: #NunCa se cumple
if a < b: #Si el valor de a es menor que el de b
if a==1 and b<c: #Si se cumplen ambas condiciones simultáneamente
if a<=b or b<=c #Si se cumple una de las dos condiciones 

#Pertenencia 
Una condicion puede ser comprobar si un valor pertenece a una lista

Para ello, podemos emplear la palabra reservada in
l=["Hola","Adíos"] 
if "Hola" in l: #Se cumple
if "adíos" in l: #No se cumple  !las mayusculas importan¡   
"""

l=["Hola","Adíos"] 
if "Hola" in l:
    print("Hola esta en la lista")
if "adíos" in l:
    print("adíos esta en la lista")
