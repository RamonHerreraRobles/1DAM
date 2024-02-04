#usuario: Ramon Herrera

#***********************************ENUNCIADO*********************************
#Hacer un programa que inicialice una lista de números con valores aleatorios 
#(10 valores), y posterior ordene los elementos de menor a mayor.

import random

lista_herrera=[random.randint(1, 100) for _ in range(10)]

lista_herrera.sort()

print("Lista:",lista_herrera)