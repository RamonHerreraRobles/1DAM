##usuario: Ramon Herrera
#************************************ENUNCIADO********************************
#Realiza un programa que pida por teclado el resultado (dato entero) obtenido al 
#lanzar un dado de seis caras y muestre por pantalla el número en letras (dato cadena) 
#de la cara opuesta al resultado obtenido.

#Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
#Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el 
#mensaje: “ERROR: número incorrecto.”.
#Ejemplo:

#Introduzca número del dado: 5
#En la cara opuesta está el "dos"
#****************************************************************************

dado = int(input("Introduzca número del dado: "))
if 1 == dado:
    print("En la cara opuesta está el 6")
elif 2 == dado:
    print("En la cara opuesta está el 5")
elif 3 == dado:
    print("En la cara opuesta está el 4")
elif 4 == dado:
    print("En la cara opuesta está el 3")
elif 5 == dado:
    print("En la cara opuesta está el 2")
elif 6 == dado:
    print("En la cara opuesta está el 1")
else:
    print("ERROR: número incorrecto.")