#usuario: Ramon Herrera

#*****************************ENUNCIADO***********************************
#Introducir una cadena de caracteres e indicar si es un palíndromo. Una palabra 
#palíndroma es aquella que se lee igual adelante que atrás.

cadena_herrera=input("introduce una cadena: ")

cadena_herrera=cadena_herrera.replace(" ","").lower()

print(cadena_herrera)
print(cadena_herrera[::-1])

if cadena_herrera==cadena_herrera[::-1]:
    print("La cadena introducida es un palindromo")
else:
    print("La cadena no es un palindromo")