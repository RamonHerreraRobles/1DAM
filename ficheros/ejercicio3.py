#usuario: Ramon Herrera

#*********************************ENUNCIADO************************
#Escribir un programa que pida dos números n y m entre 1 y 10, lea el 
#fichero primerapellido-n.txt con la tabla de multiplicar de ese número, 
#y muestre por pantalla la línea m del fichero. Si el fichero no existe 
#debe mostrar un mensaje por pantalla informando de ello.

apellido_herrera = input("Introduce el primer apellido: ").lower()

n_herrera = int(input("Introduce el número n: "))

m_herrera = int(input("Introduce el número m: "))

while n_herrera < 1 or n_herrera > 10 or m_herrera < 1 or m_herrera > 10:
    print("Número incorrecto. Introduce un número entero entre 1 y 10:")
    n_herrera = int(input("Introduce el número n: "))
    m_herrera = int(input("Introduce el número m: "))


fichero_herrera = f"{apellido_herrera}-{n_herrera}.txt"

try:
    with open(fichero_herrera, "r") as f:
        linea_herrera = f.readlines()
        print(linea_herrera[m_herrera-1])
except FileNotFoundError:
    print("El fichero",fichero_herrera,"no existe.")