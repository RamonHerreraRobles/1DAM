#usuario: Ramon Herrera

#********************************ENUNCIADO************************
#El día juliano correspondiente a una fecha es un número entero que 
#indica los días que han transcurrido desde el 1 de enero del año indicado. 
#Queremos crear un programa principal que al introducir una fecha 
#nos diga el día juliano que corresponde. Para ello podemos hacer 
#las siguientes subrutinas:

#LeerFecha: Nos permite leer por teclado una fecha (día, mes y año).
#DiasDelMes: Recibe un mes y un año y nos dice los días de ese mes en ese año.
#EsBisiesto: Recibe un año y nos dice si es bisiesto.
#Calcular_Dia_Juliano: recibe una fecha y nos devuelve el día juliano.

from funciones import LeerFecha as fecha_herrera
from funciones import DiasDelMes as diasdelmes_herrera
from funciones import Calcular_Dia_Juliano as juliano_herrera

dia_herrera, mes_herrera, anyo_herrera = fecha_herrera()
while True:
    if dia_herrera > diasdelmes_herrera(mes_herrera, anyo_herrera):
        print("El día ingresado es mayor al máximo día del mes. Intente de nuevo.")
    else:
        break
print("El día juliano correspondiente a la fecha ingresada es: ", juliano_herrera(dia_herrera, mes_herrera, anyo_herrera))

