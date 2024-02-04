#usuario: Ramon Herrera

#********************************ENUNCIADO********************************
#Crea una aplicación que pida un número y calcule su factorial (El factorial 
#de un número es el producto de todos los enteros entre 1 y el propio número y 
#se representa por el número seguido de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120),

# Pedir al usuario que ingrese un número
num_herrera = int(input("Ingrese un número: "))

# Crear una variable para almacenar el resultado del factorial
factorial_herrera = 1

# Iterar a través de todos los números entre 1 y el número ingresado
for i_herrera in range(1, num_herrera + 1):
    # Multiplicar el resultado del factorial por el número actual
    factorial_herrera *= i_herrera

# Imprimir el resultado del factorial
print("El factorial de", num_herrera , "es" ,factorial_herrera)