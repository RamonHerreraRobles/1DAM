#usuario: Ramon herrera

#***********************************ENUNCIADO*****************************
#Realizar un algoritmo que pida números (se pedirá por teclado la cantidad 
#de números a introducir). El programa debe informar de cuantos números 
#introducidos son mayores que 0, menores que 0 e iguales a 0.

# Pedir al usuario que ingrese un número
cantidad_herrera = int(input("Ingrese la cantidad de números a introducir: "))

# Crear una variable para almacenar los resultados
mayores_herrera = 0
menores_herrera = 0
iguales_herrera = 0

# Iterar a través de todos los números ingresados
for i_herrera in range(cantidad_herrera):
    # Pedir al usuario que ingrese un número
    num_herrera = int(input("Ingrese el número " + str(i_herrera + 1) + " : "))

    # Comprobar si el número es mayor que 0, menor que 0 o igual a 0
    if num_herrera > 0:
        mayores_herrera += 1
    elif num_herrera < 0:
        menores_herrera += 1
    else:
        iguales_herrera += 1

# Imprimir el resultado
print(mayores_herrera, "números introducidos son mayores que 0.")
print(menores_herrera, "números introducidos son menores que 0.")
print(iguales_herrera, "números introducidos son iguales a 0.")