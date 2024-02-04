#usuario:Ramon Herrera

#************************************ENUNCIADO*******************************
#Crear un programa que añada números a una lista hasta que introducimos un número 
#negativo. A continuación debe crear una nueva lista igual que la anterior pero 
#eliminando los números duplicados. Muestra esta segunda lista para comprobar que 
#hemos eliminados los duplicados.

numeros_herrera = []
sin_duplicados_herrera = []

while True:
    try:
        num_herrera = int(input("Introduce un número: "))
        if num_herrera < 0:
            break
        else:
            numeros_herrera.append(num_herrera)
    except ValueError:
        print("Introduce un número válido.")

for numero_herrera in numeros_herrera:
    if numero_herrera not in sin_duplicados_herrera:
        sin_duplicados_herrera.append(numero_herrera)

print("Lista sin duplicados:", sin_duplicados_herrera)