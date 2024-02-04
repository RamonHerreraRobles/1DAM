#usuario:Ramon Herrera

#************************************ENUNCIADO*******************************
#Diseñar el algoritmo correspondiente a un programa, que:

#   -Crea una tabla bidimensional de longitud 5x15 y nombre ‘marco’.
#   -Carga la tabla con dos únicos valores 0 y 1, donde el valor uno ocupará las 
#posiciones o elementos que delimitan la tabla, es decir, las más externas, 
#mientras que el resto de los elementos contendrán el valor 0.

#  111111111111111
#  100000000000001
#  100000000000001
#  100000000000001
#  111111111111111
#   -Visualiza el contenido de la matriz en pantalla.

# Crea la tabla
marco_herrera = [[0 for i in range(15)] for j in range(5)]

# Carga la tabla con valores
for i in range(5):
    for j in range(15):
        if i == 0 or i == 4 or j == 0 or j == 14:
            marco_herrera[i][j] = 1
        else:
            marco_herrera[i][j] = 0

# Visualiza el contenido de la matriz
for fila_herrera in marco_herrera:
    print(" ".join([str(num) for num in fila_herrera]))