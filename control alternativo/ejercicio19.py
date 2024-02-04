##usuario: Ramon Herrera
#************************************ENUNCIADO********************************
#Escribe un programa que pida un número entero entre uno y doce e imprima el 
#número de días que tiene el mes correspondiente.
#****************************************************************************

num=int(input("Introduzca un numero del mes (1-12): "))

if num==2: 
    print ("Este mes tiene 28 dias (excepto los años bisiestos)")
elif num==1 or num==3 or num==5 or num==7 or num==8 or num==10 or num==12:
    print ("Este mes tiene 31 dias")
else:
    print ("Este mes tiene 30 dias")