"""Una estructura de datos e un tipo de dato que permite almacenar múltiples valores. Támbien se  denominan <<colecciones>>""" 
"""En Python, existen dos grandes tipos de colecciones 
Listas: almacenan valores uno tras otro
Dicccionario: alamacena valores asociados a una clave  """

li=[1,"Hola",True,1.65]
# Añadir un elemento al final de una lista empleando <<append>>
li.append(5)
# Podemos insertar un elemento en una posicion arbitraria con <<insert>>
li.insert(1,"Nose")
print(li)
# Podemos eliminar un elemento existente en la lista con <<remove>> 
li.remove(5)
print(li)
# Podemos eliminar un elemento existente en la lista dada su posición con <<del>>
del li[1]
print(li)
# Acceso a elementos mediante un indice
li[3]
li[1] # Podemos obtener elementos de una lista mediante su posición

li[-1]
li[-2] #Podemos emplear indices negativos para empezar a contar desde el final
"""
# Acceso a elementos mediante rangos
# Se puede obtener una sublista empleando rangos
Para ello entre corchetes, se indica los extremos de la sublista separado por <<:>>
"""
li[1:3]
# Podemos no indicar algunos de los extremos. En ese caso, se considera el inicio o final
li[1:]

"""
# Actualizacion de un elemento
# El valor de un elemento se ouede modificarmediante una asignación
"""
li[1]="¿qué tal?"

"""
Operaciones básicas
"""
len(li)#Podemos emplear len para conocer la longitud de una lista

#Podemos concatebar <<+>> li+li2

print("¿qué tal?" in li) #podemos emplear in para comprobar si un elemento pertenece a una lista

"""Si tenemos una lista numerica podemos sumar sus valores empleando <<sum>>"""

lis=[1,2,3,4]

sum(lis)

"""Podemos invertir el orden de los elementos empleando <<reversed>>"""

reversed(lis)

"""Podemos reordenar los elemenetos empleando sorted"""

sorted(lis)