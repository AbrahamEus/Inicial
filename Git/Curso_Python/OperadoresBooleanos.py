#Operadores Booleanos
"""
Permite operar con valores binarios.
Los Operadores habituales son:
AND (and, &) Devuelve true si ambos valores son true
OR (or,|) Devuelve true si al menos uno de los valores es true 
NOT (not) Invierte el valor: devuelve true si el valor es falce y viceversa
XOR (^) Devuelve true si los dos valores son distintos
"""
valor1 = True & True
valor2 = False | True
valor3 = not False
valor4 = True ^ True
print(f"El valor de AND es {valor1} El valor de OR es {valor2} El valor de NOT es {valor3} El valor de XOR es {valor4}")
