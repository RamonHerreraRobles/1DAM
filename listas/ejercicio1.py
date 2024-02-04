#usuario: Ramon Herrera

#***********************************ENUNCIADO*********************************
#Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) 
#y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.

import random

lista_herrera=[random.randint(1, 10) for _ in range(10)]

for num_herrera in lista_herrera:
    cuadrado_herrera=num_herrera*num_herrera
    cubo_herrera=cuadrado_herrera*num_herrera
    print("numero:",num_herrera)
    print("cuadrado:",cuadrado_herrera)
    print("cubo:",cubo_herrera)
    print("---------------------------")