#usuario: Ramon Herrera

#***********************************ENUNCIADO*********************************
#Diseñar el algoritmo correspondiente a un programa, que:

#   -Crea una tabla bidimensional de longitud 5x5 y nombre ‘diagonal’.
#   -Carga la tabla de forma que los componentes pertenecientes a la diagonal 
#de la matriz tomen el valor 1 y el resto el valor 0.
#   -Muestra el contenido de la tabla en pantalla.

diagonal_herrera = [[0]*5 for _ in range(5)]

for i in range(5):
    diagonal_herrera[i][i] = 1
    diagonal_herrera[i][4-i] = 1

for i in range(5):
    for j in range(5):
        print(diagonal_herrera[i][j], end=' ')
    print()