#usuario: Ramon Herrera

#*****************************ENUNCIADO***********************************
#Si tenemos una cadena con un nombre y apellidos, realizar un programa que muestre las iniciales en mayúsculas.

nombre_herrera = input("Introduce un nombre y apellidos: ")
palabras_herrera = nombre_herrera.split()
iniciales_herrera = [letra_herrera[0] for letra_herrera in palabras_herrera]
siglas_herrera = ''.join(iniciales_herrera)

print(siglas_herrera.upper())