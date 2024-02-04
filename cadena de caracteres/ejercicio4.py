#usuario: Ramon Herrera

#*****************************ENUNCIADO***********************************
#Suponiendo que hemos introducido una cadena por teclado que representa una 
#frase (palabras separadas por espacios), realiza un programa que cuente cuantas palabras tiene.

frase_herrera=input("Introduzca una frase:")
palabras_herrera = frase_herrera.split()
cantidad_herrera=len(palabras_herrera)

print("La frase '"+frase_herrera+"' tiene",cantidad_herrera,"palabra/s")