#usuario: Ramon Herrera

#******************************ENUNCIADO********************************
#Escribe un programa que lea una cadena y devuelva un diccionario con la 
#cantidad de apariciones de cada carácter en la cadena.

print("Introduce una cadena: ")
biblioteca_herrera = {}

for char_herrera in input():
    if char_herrera in biblioteca_herrera:
        biblioteca_herrera[char_herrera] += 1
    else:
        biblioteca_herrera[char_herrera] = 1

print(biblioteca_herrera)