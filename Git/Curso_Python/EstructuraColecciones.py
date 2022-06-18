"""Un conjunto es una colección similar a una lista, con dos diferencias fundamentales:
*No permite almacenar valores repetidos.
*Los elementos no tiene un orden concreto.
"""

#Los conjuntos se crean empleando llaves <<{}>>

s={1,3,2}

#Se pueden añadir elementos empleando add:

s.add(4) #{1,3,2,4}
s.add(1) #{1,3,2,4} ¡Recordemos que no hay repetidos!

#No se puede acceder a los elementos por índice. Los conjuntos son útiles en algunas ocasiones por una cuestión de rendimiento, pero su uso no es tan frecuente