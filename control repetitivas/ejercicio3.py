#usuario: Ramon Herrera

#********************************ENUNCIADO*********************************
#Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir 
#la suma y la media de todos los números introducidos.

# Crear una lista vacía para almacenar los números
numeros_herrera = []

# Pedir números al usuario hasta que se introduzca un cero
while True:
    numero_herrera = int(input("Introduce un número (0 para terminar): "))
    if numero_herrera == 0:
        break
    numeros_herrera.append(numero_herrera)

# Si se han introducido números, calcular la suma y la media
if numeros_herrera:
    suma_herrera = sum(numeros_herrera)
    media_herrera = suma_herrera / len(numeros_herrera)

    print("La suma de los números introducidos es:", suma_herrera)
    print("La media de los números introducidos es:", media_herrera)
else:
    print("No se han introducido números.")