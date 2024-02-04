#usuario: Ramon Herrera
#****************************************ENUNCIADO******************************
#Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es 
#bisiesto si es un número divisible por 4, pero no si es divisible por 100, 
#excepto que también sea divisible por 400.
#******************************************************************************

# Leer el año de entrada
anyo = int(input("Por favor, ingrese un año: "))

# Comprobar si es bisiesto y mostrar el resultado
if anyo % 4 == 0 and (anyo % 100 != 0 or anyo % 400 == 0):
    print(f"{anyo} es un año bisiesto.")
else:
    print(f"{anyo} no es un año bisiesto.")
