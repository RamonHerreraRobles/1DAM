#usuario: Ramon Herrera

#***************************************ENUNCIADO*******************************
#Queremos guardar los nombres y la edades de los alumnos de un curso. Realiza un 
#programa que introduzca el nombre y la edad de cada alumno. El proceso de lectura 
#de datos terminará cuando se introduzca como nombre un asterisco (*) Al finalizar 
#se mostrará los siguientes datos:

#-Todos lo alumnos mayores de edad.
#-Los alumnos mayores (los que tienen más edad)
#*********************************************************************************

alumnos_herrera = []

while True:
    nombre_herrera = input("Ingrese el nombre del alumno (ingrese * para terminar): ")
    if nombre_herrera == '*':
        break
    edad_herrera = int(input("Ingrese la edad del alumno: "))
    alumnos_herrera.append((nombre_herrera, edad_herrera))


mayores_herrera = [alumno_herrera for alumno_herrera in alumnos_herrera if alumno_herrera[1] >= 18]
mayor_herrera = max(alumnos_herrera, key=lambda alumno_herrera: alumno_herrera[1])

print("Todos los alumnos mayores de edad:")
for alumno_herrera in mayores_herrera:
    print(alumno_herrera)

print("El alumno mayor (los que tienen más edad) es:")
print(mayor_herrera)