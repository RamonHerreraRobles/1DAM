#ususario: Ramon Herrera

#*******************************ENUNCIADO*************************
#Crea una aplicación que permita adivinar un número. La aplicación 
#genera un número aleatorio del 1 al 100. A continuación va pidiendo 
#números y va respondiendo si el número a adivinar es mayor o menor 
#que el introducido,a demás de los intentos que te quedan (tienes 10 
#intentos para acertarlo). El programa termina cuando se acierta el 
#número (además te dice en cuantos intentos lo has acertado), si se 
#llega al limite de intentos te muestra el número que había generado.

import random

print("Bienvenido al juego de adivinar el número.")
print("Estoy pensando en un número del 1 al 100.")
print("Tienes 10 intentos para adivinar el número.")

numero_secreto_herrera = random.randint(1, 100)
intentos_herrera = 10

while intentos_herrera > 0:
    numero_herrera = int(input("Intenta adivinar el número: "))

    if numero_herrera < numero_secreto_herrera:
        print("El número secreto es mayor que tu número.")
    elif numero_herrera > numero_secreto_herrera:
        print("El número secreto es menor que tu número.")
    else:
        print("¡Felicidades! Adivinaste el número secreto.")
        print("Número de intentos utilizados:", 10 - intentos_herrera)
        break

    intentos_herrera -= 1

if intentos_herrera == 0:
    print("¡Te has quedado sin intentos! El número que pensaba era:", numero_secreto_herrera)