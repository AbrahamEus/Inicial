"""
Un Diccionario es una coleccion no ordenada de valores asociados a una clave. En un diccionario, cada clave es única (no hay repetidas). 
En Python, declaramos un diccionario vacío con llaves:
"""

d={} # Diccionario vacío

"""Podemos declarar un diccionario con datos desde el inicio. Para ello, los elementos se separan por comas y las claves se separan de los valores empleando <<:>>"""

d={"c1":1, 3:"Hola","b2":True,"a_":1.4}

#Inserción de nuevos elementos
#Podemos insertar un nuevo elemento mediante una asignacion:
d["d7"] = "mundo" # Entre corchetes se indica la clave
#A dicha clave se le asocia el valor indicado

del d["c1"]# Borrar elemento mediante la clave

d["a_"]# Acceso a elementos mediante la clave

d["d7"] = "Adiós"# Actualizacion de un elemento

"""Diccionarios Operaciones"""

# Podemos emplear len para conocer la longuitud de un diccionario

len(d)

# Podemos comprobar si una clave exite empleando in

"Adiós" in d

# Podemos usar keys y values para recuperar las claves y valores de un diccionario
d.keys()
d.values()
