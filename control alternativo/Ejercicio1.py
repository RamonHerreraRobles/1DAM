#Usuario: Ramon Herrera
#************************************ENUNCIADO***************************************
#Algoritmo que pida dos números e indique si el primero es mayor que el segundo o no.
#************************************************************************************

print("Ingrese los dos números que desea comparar:")

# Pide el primer número al usuario
numero1 = int(input("Ingrese el primer número: "))

# Pide el segundo número al usuario
numero2 = int(input("Ingrese el segundo número: "))

# Compara los números
if numero1 > numero2:
    print("El primer número es mayor que el segundo.")
else:
    print("El segundo número es mayor que el primero.")