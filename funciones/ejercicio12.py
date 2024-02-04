#usuario: Ramon Herrera

#********************************ENUNCIADO************************
#Vamos a mejorar el ejercicio anterior haciendo una función para 
#validar la fecha. De tal forma que al leer una fecha se asegura que es válida.

from funciones import LeerFecha as fecha_herrera
from funciones import Calcular_Dia_Juliano as juliano_herrera
from funciones import Valido as valido_herrera

dia_herrera, mes_herrera, anyo_herrera = fecha_herrera()

if valido_herrera(dia_herrera, mes_herrera, anyo_herrera):
    dia_juliano_herrera = juliano_herrera(dia_herrera, mes_herrera, anyo_herrera)
    print("El día juliano correspondiente a la fecha {}-{}-{} es: {}".format(dia_herrera, mes_herrera, anyo_herrera, dia_juliano_herrera))
else:
    print("La fecha ingresada no es válida.")