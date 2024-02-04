#usuario: Ramon Herrera

#******************************ENUNCIADO********************************
#Codifica un programa en python que nos permita guardar los nombres de los 
#alumnos de una clase y las notas que han obtenido. Cada alumno puede tener 
#distinta cantidad de notas. Guarda la información en un diccionario cuya 
#claves serán los nombres de los alumnos y los valores serán listas con las notas de cada alumno.

#El programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre 
#e irá pidiendo sus notas hasta que introduzcamos un número negativo. Al final el 
#programa nos mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos. 
#Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará un error.

biblioteca_herrera = {}

alumnos_herrera = int(input("Introduce el número de alumnos que se van a introducir: "))

for i in range(alumnos_herrera):
    nombre_herrera = input("Introduce el nombre del alumno: ")

    if nombre_herrera in biblioteca_herrera:
        print("Error: El nombre del alumno ya existe.")
        continue

    biblioteca_herrera[nombre_herrera] = []

    while True:
        nota_herrera = float(input("Introduce la nota del alumno: "))

        if nota_herrera < 0:
            break

        biblioteca_herrera[nombre_herrera].append(nota_herrera)

for nombre_herrera, notas_herrera in biblioteca_herrera.items():
    media_herrera = sum(notas_herrera) / len(notas_herrera)

    print(f"Nombre del alumno: {nombre_herrera}")
    print(f"Notas: {notas_herrera}")
    print(f"Nota media: {media_herrera}")
    print("")