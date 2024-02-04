#usuario: Ramon Herrera

#*******************************ENUNCIADO****************************
#Una empresa les paga a sus empleados con base en las horas trabajadas 
#en la semana. Para esto, se registran los días que trabajó y las horas 
#de cada día. Realice un algoritmo para determinar el sueldo semanal de 
#N trabajadores y además calcule cuánto pagó la empresa por los N empleados.

horas_herrera=1
contador_herrera=0
total_herrera=0
while horas_herrera!=0:
    horas_herrera=int(input("¿Cuantas horas trabaja al dia este empleado?(Introduzca 0 para terminar) "))
    if (horas_herrera==0):
        break
    dias_herrera=int(input("¿Cuantos dias trabaja este empleado?"))
    sueldo_herrera=float(input("¿Cuanto cobra este empleado por hora?"))
    empleado_herrera=sueldo_herrera*horas_herrera*dias_herrera
    contador_herrera=contador_herrera+1
    print("Este empleado cobrara",empleado_herrera,"euros a la semana")
    total_herrera=total_herrera+empleado_herrera

print("Una empresa con",contador_herrera,"empleados, pagara",total_herrera,"euros en total a la semana")