#usuario: Ramon Herrera

#********************************ENUNCIADO************************
#Escribir dos funciones que permitan calcular:

#-La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
#-La cantidad de horas, minutos y segundos de un tiempo dado en segundos.

#Escribe un programa principal con un menú donde se pueda elegir la opción 
#de convertir a segundos, convertir a horas,minutos y segundos o salir del programa.


from funciones import horas_minutos_segundos_a_segundos as hora_herrera
from funciones import segundos_a_horas_minutos_segundos as cronometro_herrera

while True:
    print("Seleccione una opción:")
    print("1. Convertir a segundos")
    print("2. Convertir a horas, minutos y segundos")
    print("3. Salir")
    opcion_herrera = input()
    if opcion_herrera == '1':
        horas_herrera = int(input("Ingrese las horas: "))
        minutos_herrera = int(input("Ingrese los minutos: "))
        segundos_herrera = int(input("Ingrese los segundos: "))
        total_herrera = hora_herrera(horas_herrera, minutos_herrera, segundos_herrera)
        print("La cantidad de segundos en total es:", total_herrera)
    elif opcion_herrera == '2':
        segundos_herrera = int(input("Ingrese la cantidad de segundos: "))
        horas_herrera, minutos_herrera, segundos_herrera = cronometro_herrera(segundos_herrera)
        print("La cantidad de horas, minutos y segundos en total es:", horas_herrera, "horas", minutos_herrera, "minutos y", segundos_herrera, "segundos")
    elif opcion_herrera == '3':
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Intente nuevamente.")

