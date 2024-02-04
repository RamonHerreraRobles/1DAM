#usuario: Ramon Herrera

#***************************************ENUNCIADO*******************************
#Diseñar el algoritmo correspondiente a un programa, que:

#-Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
#-Carga la tabla con valores numéricos enteros.
#-Suma todos los elementos de cada fila y todos los elementos de cada columna visualizando los resultados en pantalla.
#*********************************************************************************

tabla_herrera = [[0]*5 for _ in range(5)]

for i in range(5):
    for j in range(5):
        tabla_herrera[i][j] = int(input(f"Ingrese el valor para la posición ({i},{j}): "))

filas_herrera = [0]*5
columnas_herrera = [0]*5

for i in range(5): 
    for j in range(5):
        filas_herrera[i] += tabla_herrera[i][j]
        columnas_herrera[j] += tabla_herrera[i][j]

# Mostrar la tabla
print("\nTabla:")
for fila_herrera in tabla_herrera:
    print(fila_herrera)
    
print("Suma de las filas:", filas_herrera)
print("Suma de las columnas:", columnas_herrera)