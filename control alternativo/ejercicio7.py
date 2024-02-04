#Usuario: Ramon Herrera
#**********************************ENUNCIADO**************************************
#Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir tres cosas:

#   - El exponente sea positivo, sólo tienes que imprimir la potencia.
#   - El exponente sea 0, el resultado es 1.
#   - El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

#*********************************************************************************

# Solicitar la base por teclado
base = int(input("Ingrese la base: "))

# Solicitar el exponente por teclado
exponente = int(input("Ingrese el exponente: "))

# Crear un condicional que verifique el valor del exponente
if exponente > 0:
    # Si el exponente es positivo, imprimir la potencia
    print("La potencia de la base", base, "con el exponente", exponente, "es: ", base ** exponente)
elif exponente == 0:
    # Si el exponente es 0, imprimir 1
    print("El resultado es 1")
else:
    # Si el exponente es negativo, imprimir 1/potencia
    print("La potencia de la base", base, "con el exponente", exponente, "es: ", 1 / (base ** -exponente))