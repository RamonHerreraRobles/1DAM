#usuario: Ramon Herrera

#********************************ENUNCIADO************************
#Crear una función recursiva que permita calcular el factorial de un 
#número. Realiza un programa principal donde se lea un entero y se 
#muestre el resultado del factorial.

from funciones import factorial as factorial_herrera

num_herrera = int(input("Ingrese un número entero: "))
print("El factorial de", num_herrera, "es:", factorial_herrera(num_herrera))
