#usuario: Ramon Herrera

#********************************ENUNCIADO************************
#Crear una función que calcule la temperatura media de un día a partir 
#de la temperatura máxima y mínima. Crear un programa principal, 
#que utilizando la función anterior, vaya pidiendo la temperatura 
#máxima y mínima de cada día y vaya mostrando la media. El programa 
#pedirá el número de días que se van a introducir.

dias_herrera = int(input("Introduce el número de días que deseas introducir: "))

from funciones import calcular_temperatura_media as media_herrera

for i in range(dias_herrera):
    max_herrera = float(input("Introduce la temperatura máxima del día " + str(i+1) + ": "))
    min_herrera = float(input("Introduce la temperatura mínima del día " + str(i+1) + ": "))
    
    temp_herrera = media_herrera(max_herrera, min_herrera)
    print("La temperatura media del día " + str(i+1) + " es: " + str(temp_herrera))
