#usuario: Ramon herrera

#***********************************ENUNCIADO*****************************
#Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

# Solicitar los dos números al usuario
num1_herrera = int(input("Ingrese el primer número: "))
num2_herrera = int(input("Ingrese el segundo número: "))

# Comprobar si num1 es menor que num2
if num1_herrera < num2_herrera:
    while num1_herrera<=num2_herrera:
        if num1_herrera%2 == 0 :
            print (num1_herrera)
            num1_herrera=num1_herrera+1
        else:
            num1_herrera=num1_herrera+1
else:
    if num1_herrera==num2_herrera:
        print("Ambos numeros son iguales")
    else:
      while num2_herrera<=num1_herrera:
        if num2_herrera%2 == 0 :
            print (num1_herrera)
            num2_herrera=num2_herrera+1
        else:
            num1_herrera=num1_herrera+1