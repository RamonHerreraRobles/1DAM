#Usuario: Ramon Herrera
#**********************************ENUNCIADO**************************************
#Escribe un programa que lea un número e indique si es par o impar.
#*********************************************************************************

print("Ingrese un número:")
numero = int(input())

if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")