##usuario: Ramon Herrera
#************************************ENUNCIADO********************************
#Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día 
#correspondiente. Si introducimos otro número nos da un error.
#****************************************************************************

dia= int(input("introduzca un numero de la semana(1-7): "))

if 1 == dia: 
    print ("Lunes")
elif 2 == dia:
    print ("Martes")
elif 3 == dia:
    print ("Miercoles")
elif 4 == dia:
    print ("Jueves")
elif 5 == dia:
    print ("Viernes")
elif 6 == dia:
    print ("Sabado")
elif 7== dia: 
    print ("Domingo")
else:
    print ("Error, introduce un valor valido del 1 al 7.")