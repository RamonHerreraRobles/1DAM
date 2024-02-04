#Usuario: Ramon Herrera
#**********************************ENUNCIADO**************************************
#Programa que lea una cadena por teclado y compruebe si la primera letra es una mayúscula o no.
#*********************************************************************************

print("Ingrese una cadena:")
cadena = input()

if cadena:
    primera_letra = cadena[0]

    if primera_letra.isupper():
        print("La primera letra es una mayúscula.")
    else:
        print("La primera letra no es una mayúscula.")
else:
    print("La cadena está vacía.")