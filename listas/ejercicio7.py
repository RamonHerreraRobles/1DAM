#usuario: Ramon Herrera

#***************************************ENUNCIADO*******************************
#Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco enteros 
#cada uno, pida valores para ‘lista1’ y ‘lista2’ y calcule lista3=lista1+lista2.
#*********************************************************************************

lista1_herrera = [int(input(f"Ingrese un entero para la posición {i+1} de la lista 1: ")) for i in range(5)]
lista2_herrera = [int(input(f"Ingrese un entero para la posición {i+1} de la lista 2: ")) for i in range(5)]

lista3_herrera = [a + b for a, b in zip(lista1_herrera, lista2_herrera)]

print("Lista 1:",lista1_herrera,"+ Lista 2:",lista2_herrera,"= Lista 3", lista3_herrera)