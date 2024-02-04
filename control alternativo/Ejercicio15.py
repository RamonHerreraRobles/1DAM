##usuario: Ramon Herrera
#************************************ENUNCIADO********************************
#El director de una escuela está organizando un viaje de estudios, y requiere 
#determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía 
#de viajes por el servicio. La forma de cobrar es la siguiente: si son 100 
#alumnos o más, el costo por cada alumno es de 65 euros; de 50 a 99 alumnos, 
#el costo es de 70 euros, de 30 a 49, de 95 euros, y si son menos de 30, el 
#costo de la renta del autobús es de 4000 euros, sin importar el número de 
#alumnos. Realice un algoritmo que permita determinar el pago a la compañía 
#de autobuses y lo que debe pagar cada alumno por el viaje.
#****************************************************************************

num_alumnos = int(input("Ingrese el número de alumnos: "))

if num_alumnos >= 100:
    costo_alumno = 65
elif 50 <= num_alumnos < 100:
    costo_alumno = 70
elif 30 <= num_alumnos < 50:
    costo_alumno = 95
else:
    costo_alumno = 4000 / num_alumnos

total_costo = num_alumnos * costo_alumno
print("Cada alumno debe pagar:", costo_alumno, "euros.")
print("El director debe pagar a la compañía de autobuses:", total_costo, "euros.")