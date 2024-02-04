#usuario: Ramon Herrera

#*********************************ENUNCIADO************************
#Escribir un programa que pida un número entero entre 1 y 10, lea el 
#fichero primerapellido-n.txt con la tabla de multiplicar de ese número, 
#donde n es el número introducido, y la muestre por pantalla. Si el fichero 
#no existe debe mostrar un mensaje por pantalla informando de ello.

apellido_herrera = input("Introduce tu primer apellido: ").lower()

n_herrera = int(input("Introduce un número entero entre 1 y 10:"))

while n_herrera < 1 or n_herrera > 10:
    print("Número incorrecto. Introduce un número entero entre 1 y 10:")
    n_herrera = int(input())

fichero_herrera = f"{apellido_herrera}-{n_herrera}.txt"

try:
    with open(fichero_herrera, "r") as f:
        tabla_herrera = f.read()
        print(tabla_herrera)
except FileNotFoundError:
    print("El fichero",fichero_herrera,"no existe.")