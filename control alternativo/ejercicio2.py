#Usuario: Ramon Herrera
#**********************************ENUNCIADO**************************************
#Algoritmo que pida un número y diga si es positivo, negativo o 0.
#*********************************************************************************

print("Ingrese un número:")
numero = int(input())

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es 0.")