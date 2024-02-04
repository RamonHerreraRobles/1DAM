#usuario: Ramon Herrera

#*******************************ENUNCIADO****************************
#Una empresa tiene el registro de las horas que trabaja diariamente un 
#empleado durante la semana (seis días) y requiere determinar el total 
#de éstas, así como el sueldo que recibirá por las horas trabajadas.

dias_herrera=1
sueldo_herrera=0
sueldo_dia_herrera=0
cont_horas_herrera=0

dinero_herrera=float(input("Introduzca el dinero que cobra el empleado por hora:"))
while dias_herrera<=6:
    print("DIA ",dias_herrera)
    horas_herrera=int(input("Introduzca las horas trabajadas durante este dia:"))
    sueldo_dia_herrera=dinero_herrera*horas_herrera
    sueldo_herrera=sueldo_herrera+sueldo_dia_herrera
    cont_horas_herrera=cont_horas_herrera+horas_herrera
    dias_herrera=dias_herrera+1

print("El empleado ha trabajado",cont_horas_herrera,"horas")
print("Y su salario es de ",sueldo_herrera)