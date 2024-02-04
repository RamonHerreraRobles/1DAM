#usuario: Ramon Herrera

#*******************************ENUNCIADO****************************
#Escribe un programa que diga si un número introducido por teclado es o 
#no primo. Un número primo es aquel que sólo es divisible entre él mismo 
#y la unidad. Nota: Es suficiente probar hasta la raíz cuadrada del número 
#para ver si es divisible por algún otro número.

num_herrera = int(input("Introduce un número: "))
primo_herrera = True

if num_herrera <= 1:
    primo_herrera = False
else:
    for i in range(2, int(num_herrera**0.5) + 1):
        if num_herrera % i == 0:
            primo_herrera = False
            break

if primo_herrera:
    print(num_herrera, "es un número primo.")
else:
    print(num_herrera, "no es un número primo.")