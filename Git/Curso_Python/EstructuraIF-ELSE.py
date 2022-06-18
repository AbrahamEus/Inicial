"""
Podemos emplear la estructura if-else para ejecutar código si no se cumple la condición:
"""
#Sintaxis
if 1<2 :
    print(1+2) #La palabra <<else>> indica que el codigo se ejecutará si no se cumple la condición
else:  #La palabra <<else>> significa <<si no>> o <<en otro caso>> en ingles
    print("No se cumplio la condicion")    

"""
La estructura if-elif-else
De forma similar, podemos emplear la estructura if-elif-else para gestionar varias condiciones:
"""        
nota = 7
if nota < 5:
    print("Suspenso")
elif nota < 7:
     print("Suspenso")
elif nota < 9:
     print("Notable")
elif nota < 10:
    print("Sobresaliente")
else:
    print("Matricula de honor") 

