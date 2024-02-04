# Pedir la cadena por teclado
cadena = input("Ingrese una cadena de varias palabras: ")

# Pedir el carácter por teclado
caracter = input("Ingrese un carácter por teclado: ")

# Convertir la cadena en minúsculas
cadena_minusculas = cadena.lower()

# Contar la cantidad de veces que aparece el carácter en la cadena
contador = cadena_minusculas.count(caracter)

# Mostrar el resultado
print("El carácter '{}' aparece {} veces en la cadena.".format(caracter, contador))