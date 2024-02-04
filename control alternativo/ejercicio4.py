#Usuario: Ramon Herrera
#**********************************ENUNCIADO**************************************
#Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de aviso en caso contrario.
#*********************************************************************************

print("Ingrese el primer número:")
numero1 = int(input())

print("Ingrese el segundo número:")
numero2 = int(input())

if numero2 != 0:
    division = numero1 / numero2
    print("La división del primer número entre el segundo es: ", division)
else:
    print("El segundo número no puede ser cero.")