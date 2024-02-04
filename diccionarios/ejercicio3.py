#usuario: Ramon Herrera

#******************************ENUNCIADO********************************
#Vamos a crear un programa en python donde vamos a declarar un diccionario 
#para guardar los precios de las distintas frutas. El programa pedirá el 
#nombre de la fruta y la cantidad que se ha vendido y nos mostrará el 
#precio final de la fruta a partir de los datos guardados en el diccionario. 
#Si la fruta no existe nos dará un error. Tras cada consulta el programa 
#nos preguntará si queremos hacer otra consulta.

biblioteca_herrera = {}

while True:
    fruta_herrera = input("Introduce el nombre de la fruta (Introduzca '0' para finalizar): ")
    if fruta_herrera == "0":
        break
    precio_herrera = float(input("Introduce el precio de la fruta: "))
    biblioteca_herrera[fruta_herrera] = precio_herrera

while True:
    fruta_herrera = input("Introduce el nombre de la fruta vendida: ")
    if fruta_herrera in biblioteca_herrera:
        cantidad_herrera = int(input("Introduce la cantidad vendida de la fruta: "))
        print("El precio final de la fruta a partir de los datos guardados en el diccionario es: ", biblioteca_herrera[fruta_herrera] * cantidad_herrera)
    else:
        print("Error: La fruta no existe en el diccionario.")
    consulta_herrera = input("¿Deseas hacer otra consulta? (S/N): ")
    if consulta_herrera.lower() == "n":
        break