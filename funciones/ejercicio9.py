#usuario: Ramon Herrera

#********************************ENUNCIADO************************
#Crear una función que calcule el MCD de dos número por el método de 
#Euclides. El método de Euclides es el siguiente:

#-Se divide el número mayor entre el menor.
#-Si la división es exacta, el divisor es el MCD.
#-Si la división no es exacta, dividimos el divisor entre el resto obtenido 
#y se continúa de esta forma hasta obtener una división exacta, siendo el último divisor el MCD.

#Crea un programa principal que lea dos números enteros y muestre el MCD.

from funciones import mcd as mcd_herrera
num1_herrera = int(input("Ingrese el primer número: "))
num2_herrera = int(input("Ingrese el segundo número: "))

print("El MCD de", num1_herrera, "y", num2_herrera, "es:", mcd_herrera(num1_herrera, num2_herrera))