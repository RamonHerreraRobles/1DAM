#usuario:Ramon Herrera

#********************************************ENUNCIADO***************************************
#Escriba un programa que permita crear una lista de palabras y que, a continuación de tres opciones:

#   -Contar: Me pide una cadena, y me dice cuantas veces aparece en la lista
#   -Modificar: Me pide una cadena, y otra cadena a modificar, y modifica todas alas apariciones 
#       de la primera por la segunda en la lista.
#   -Eliminar: Me pide una cadena, y la elimina de la lista.
#   -Mostrar: Muestra la lista de cadenas
#   -Terminar

cadenas_herrera = []
while True:
    print("Opciones:")
    print("1. Contar")
    print("2. Modificar")
    print("3. Eliminar")
    print("4. Mostrar")
    print("5. Introducir palabra")
    print("6. Terminar")

    opcion_herrera = int(input("Introduce el número de la opción deseada: "))

    if opcion_herrera == 1:
        palabra_herrera = input("Introduce la palabra a contar: ")
        contador_herrera = cadenas_herrera.count(palabra_herrera)
        print(f"La palabra '{palabra_herrera}' aparece {contador_herrera} veces en la lista.")
    elif opcion_herrera == 2:
        palabra_a_modificar_herrera = input("Introduce la palabra a modificar: ")
        palabra_nueva_herrera = input("Introduce la nueva palabra: ")
        cadenas_herrera = [palabra_nueva_herrera if cadena_herrera == palabra_a_modificar_herrera else cadena_herrera for cadena_herrera in cadenas_herrera]
        print(f"Las palabras '{palabra_a_modificar_herrera}' han sido modificadas por '{palabra_nueva_herrera}' en la lista.")
    elif opcion_herrera == 3:
        palabra_a_eliminar_herrera = input("Introduce la palabra a eliminar: ")
        while palabra_a_eliminar_herrera in cadenas_herrera:
            cadenas_herrera.remove(palabra_a_eliminar_herrera)
        print(f"La palabra '{palabra_a_eliminar_herrera}' ha sido eliminada de la lista.")
    elif opcion_herrera == 4:
        print("Lista de cadenas:")
        for cadena_herrera in cadenas_herrera:
            print("-",cadena_herrera)
    elif opcion_herrera == 5:
        palabra_nueva_herrera = input("Ingrese la nueva palabra a añadir: ")
        cadenas_herrera.append(palabra_nueva_herrera)
        print(f"La palabra '{palabra_nueva_herrera}' ha sido añadida a la lista.")
    elif opcion_herrera == 6:
        print("Fin del programa.")
        break
    else:
        print("Opción no válida, intente de nuevo.")