#usuario: Ramon Herrera

#******************************ENUNCIADO********************************
#Escribir un programa que implemente una agenda. En la agenda se podrán 
#guardar nombres y números de teléfono. El programa nos dará el siguiente menú:

#   -Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto. Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
#   -Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres comiencen por dicha cadena.
#   -Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
#   -Listar: Nos muestra todos los contactos de la agenda.
#   -Implementar el programa con un diccionario.

biblioteca_herrera = {}

while True:
    print("Menú:")
    print("1. Añadir/modificar")
    print("2. Buscar")
    print("3. Borrar")
    print("4. Listar")
    print("5. Salir")

    opcion_herrera = input("Ingrese una opción: ")

    if opcion_herrera == '1':
        nombre_herrera = input("Ingrese un nombre: ")
        if nombre_herrera in biblioteca_herrera:
            print("Número de teléfono:", biblioteca_herrera[nombre_herrera])
            modificar_herrera = input("¿Desea modificar el número de teléfono? (s/n): ").lower()
            if modificar_herrera == 's':
                biblioteca_herrera[nombre_herrera] = input("Ingrese el nuevo número de teléfono: ")
        else:
            biblioteca_herrera[nombre_herrera] = input("Ingrese el número de teléfono: ")
    elif opcion_herrera == '2':
        busqueda_herrera = input("Ingrese una cadena de caracteres: ")
        print("\nResultados de la búsqueda:")
        for nombre_herrera, telefono_herrera in biblioteca_herrera.items():
            if nombre_herrera.startswith(busqueda_herrera):
                print(nombre_herrera, "-", telefono_herrera)
    elif opcion_herrera == '3':
        nombre_herrera = input("Ingrese un nombre para borrarlo de la agenda: ")
        if nombre_herrera in biblioteca_herrera:
            borrar_herrera = input("¿Desea borrar a '{}' de la agenda? (s/n): ".format(nombre_herrera)).lower()
            if borrar_herrera == 's':
                del biblioteca_herrera[nombre_herrera]
                print("Contacto borrado de la agenda.")
        else:
            print("No se encontró el nombre en la agenda.")
    elif opcion_herrera == '4':
        print("\nContactos en la agenda:")
        for nombre_herrera, telefono_herrera in biblioteca_herrera.items():
            print(nombre_herrera, "-", telefono_herrera)
    elif opcion_herrera == '5':
        print("Saliendo de la agenda...")
        break
    else:
        print("Opción no válida, por favor intente de nuevo.")