#usuario:Ramon Herrera

#************************************ENUNCIADO*******************************
#Crear un programa que lea los precios de 5 artículos y las cantidades vendidas 
#por una empresa en sus 4 sucursales. Informar:

#   -Las cantidades totales de cada articulo.
#   -La cantidad de artículos en la sucursal 2.
#   -La cantidad del articulo 3 en la sucursal 1.
#   -La recaudación total de cada sucursal.
#   -La recaudación total de la empresa.
#   -La sucursal de mayor recaudación.

# Variables de control
n_articulos = 5
n_sucursales = 4

# Crear una lista vacía para almacenar los precios y cantidades vendidas
precios = []
cantidades_vendidas = []

# Crear una lista vacía para almacenar la recaudación total de cada sucursal
recaudacion_sucursales = []

# Leer los precios de los 5 artículos y almacenarlos en la lista precios
for i in range(n_articulos):
    precio = float(input(f"Ingrese el precio del articulo {i+1}: "))
    precios.append(precio)

# Leer las cantidades vendidas de cada artículo en cada sucursal y almacenarlas en la lista cantidades_vendidas
for i in range(n_sucursales):
    for j in range(n_articulos):
        cantidad = int(input(f"Ingrese la cantidad vendida del articulo {j+1} en la sucursal {i+1}: "))
        cantidades_vendidas.append(cantidad)

# Calcular la cantidad total de cada artículo en toda la empresa
cantidades_totales = []
for i in range(n_articulos):
    suma = 0
    for j in range(n_sucursales):
        suma += cantidades_vendidas[i + j*n_articulos]
    cantidades_totales.append(suma)

# Calcular la cantidad de artículos totales en la sucursal 2
cantidad_articulos_sucursal_2 = sum(cantidades_vendidas[n_articulos:2*n_articulos])

# Calcular la cantidad del artículo 3 en la sucursal 1
cantidad_articulo_3_sucursal_1 = cantidades_vendidas[n_articulos*1 + 3]

# Calcular la recaudación total de cada sucursal
for i in range(n_sucursales):
    recaudacion = 0
    for j in range(n_articulos):
        recaudacion += precios[j] * cantidades_vendidas[i + j*n_sucursales]
    recaudacion_sucursales.append(recaudacion)

# Calcular la suma de recaudación de la empresa
suma_recaudacion = sum(recaudacion_sucursales)

# Calcular la sucursal de mayor recaudación
mayor_recaudacion = max(recaudacion_sucursales)
sucursal_mayor_recaudacion = recaudacion_sucursales.index(mayor_recaudacion) + 1

# Imprimir los resultados
print("Resultados:")
print(f"-Las cantidades totales de cada articulo en toda la empresa: {cantidades_totales}")
print(f"-La cantidad de artículos totales en la sucursal 2: {cantidad_articulos_sucursal_2}")
print(f"-La cantidad del articulo 3 en la sucursal 1: {cantidad_articulo_3_sucursal_1}")
print(f"-La recaudación total de cada sucursal: {recaudacion_sucursales}")
print(f"-La suma de recaudacion de la empresa: {suma_recaudacion}")
print(f"-La sucursal de mayor recaudación: {sucursal_mayor_recaudacion}")