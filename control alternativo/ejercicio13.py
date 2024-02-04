#usuario: Ramon Herrera
#*********************************ENUNCIADO********************************
#Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta
#**************************************************************************

from datetime import datetime

while True:
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el año: "))

    try:
        datetime(anio, mes, dia)
        print("La fecha ingresada es correcta.")
        break
    except ValueError:
        print("La fecha ingresada no es correcta. Intente de nuevo.")