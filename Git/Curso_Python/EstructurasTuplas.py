"""Una tupla es una colección similar a una lista con algunas diferencias"""

#Las tuplas se crean empleando paréntesis, en el lugar de corchetes

t=(1,3,2)

# Las tuplas son inmutables: no se puede añadir, borrar ni modificar sus elementos

t[1]=0     # Esto proboca un error
del t[2]   # Esto proboca un error   
t.append(4)# Esto proboca un error

#Se emplean para algunos propósitos concretos

#Si se asignan varios valores a una variable, PYthon construye automáticamente una tupla. Esta operación recibe el nombre de <<empaquetado>> 

t = 1,2,3,4, # t = (1,2,3,4)

#En sentido contrario, si se asigna una tupla a tantas variables como elementos tenga, se <<desempaqueta>> la tupla

a,b,c,d = t # a=1, b=2, c=3, d=4

#La sintaxix que vimos anteriormente para la asignación múltiple, es una combinación del empaquetado y el desempaquetado en una sola línea de código