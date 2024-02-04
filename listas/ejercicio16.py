#usuario:Ramon Herrera

#************************************ENUNCIADO*******************************
#Vamos a crear un programa que tenga el siguiente menú:

#   -Añadir número a la lista: Me pide un número de la lista y lo añade al final de la lista.
#   -Añadir número de la lista en una posición: Me pide un número y una posición, y si la posición 
#       existe en la lista lo añade a ella (la posición se pide a partir de 1).
#   -Longitud de la lista: te muestra el número de elementos de la lista.
#   -Eliminar el último número: Muestra el último número de la lista y lo borra.
#   -Eliminar un número: Pide una posición, y si la posición existe en la lista lo borra de ella 
#       (la posición se pide a partir de 1).
#   -Contar números: Te pide un número y te dice cuantas apariciones hay en la lista.
#   -Posiciones de un número: Te pide un número y te dice en que posiciones está (contando desde 1).
#   -Mostrar números: Muestra los números de la lista
#   -Salir

lista_numeros_herrera = []

while True:
    print("\nMenú:")
    print("1. Añadir número a la lista")
    print("2. Añadir número de la lista en una posición")
    print("3. Longitud de la lista")
    print("4. Eliminar el último número")
    print("5. Eliminar un número")
    print("6. Contar números")
    print("7. Posiciones de un número")
    print("8. Mostrar números")
    print("9. Salir")

    opcion_herrera = int(input("\nIngrese el número de la opción deseada: "))

    if opcion_herrera == 1:
        numero_herrera = int(input("\nIngrese un número para añadir a la lista: "))
        lista_numeros_herrera.append(numero_herrera)
        print("\nNúmero añadido a la lista")
    elif opcion_herrera == 2:
        numero_herrera = int(input("\nIngrese un número para añadir a la lista: "))
        posicion_herrera = int(input("\nIngrese la posición en la que desea añadir el número (contando desde 1): "))
        if posicion_herrera <= len(lista_numeros_herrera) + 1:
            lista_numeros_herrera.insert(posicion_herrera - 1, numero_herrera)
            print("\nNúmero añadido a la posición especificada en la lista")
        else:
            print("\nError: la posición ingresada no existe en la lista")
    elif opcion_herrera == 3:
        print("\nLongitud de la lista: ", len(lista_numeros_herrera))
    elif opcion_herrera == 4:
        if lista_numeros_herrera:
            ultimo_numero = lista_numeros_herrera[-1]
            print("\nÚltimo número de la lista: ", ultimo_numero)
            lista_numeros_herrera.pop()
        else:
            print("\nError: la lista está vacía")
    elif opcion_herrera == 5:
        posicion_herrera = int(input("\nIngrese la posición del número que desea eliminar (contando desde 1): "))
        if posicion_herrera <= len(lista_numeros_herrera):
            eliminado_herrera = lista_numeros_herrera.pop(posicion_herrera - 1)
            print("\nNúmero eliminado de la lista: ", eliminado_herrera)
        else:
            print("\nError: la posición ingresada no existe en la lista")
    elif opcion_herrera == 6:
        numero_herrera = int(input("\nIngrese un número para contar: "))
        contador_herrera = lista_numeros_herrera.count(numero_herrera)
        print("\nEl número ", numero_herrera, " aparece ", contador_herrera, " veces en la lista")
    elif opcion_herrera == 7:
        numero_herrera = int(input("\nIngrese un número para obtener sus posiciones: "))
        posiciones_herrera = [i for i, x in enumerate(lista_numeros_herrera) if x == numero_herrera]
        if posiciones_herrera:
            print("\nEl número ", numero_herrera, " se encuentra en las posiciones: ", posiciones_herrera)
        else:
            print("\nError: el número ingresado no se encuentra en la lista")
    elif opcion_herrera == 8:
        print("\nNúmeros en la lista: ", lista_numeros_herrera)
    elif opcion_herrera == 9:
        print("\nSaliendo del programa...")
        break
    else:
        print("\nError: opción no válida")