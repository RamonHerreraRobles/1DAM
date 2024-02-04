#usuario: Ramon Herrera

#*********************************ENUNCIADO************************
#Escribir una programa que pida un número entero entre 1 y 10 y guarde 
#en un fichero con el nombre primer apellido-n.txt la tabla de multiplicar de ese número, 
#donde n es el número introducido.

apellido_herrera = input("Ingrese su apellido: ").lower()
n_herrera = int(input("Ingrese un número entero entre 1 y 10: "))

while n_herrera < 1 or n_herrera > 10:
    print("Número fuera de rango, ingrese otro número entero entre 1 y 10: ")
    n_herrera = int(input("Ingrese un número entero entre 1 y 10: "))

fichero_herrera = f"{apellido_herrera}-{n_herrera}.txt"


with open(fichero_herrera, "w") as f:
    for i in range(1, 11):
        f.write(f"{n_herrera} x {i} = {n_herrera*i}\n")

print("Tabla guardada en el archivo",fichero_herrera)