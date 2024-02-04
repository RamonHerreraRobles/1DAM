#usuario: Ramon Herrera
#************************************ENUNCIADO********************************
#La asociación de vinicultores tiene como política fijar un precio inicial al kilo 
#de uva, la cual se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando 
#se realiza la venta del producto, ésta es de un solo tipo y tamaño, se requiere 
#determinar cuánto recibirá un productor por la uva que entrega en un embarque, 
#considerando lo siguiente: si es de tipo A, se le cargan 20 céntimos al precio inicial 
#cuando es de tamaño 1; y 30 céntimos si es de tamaño 2. Si es de tipo B, se rebajan 
#30 céntimos cuando es de tamaño 1, y 50 céntimos cuando es de tamaño 2. Realice 
#un algoritmo para determinar la ganancia obtenida.
#****************************************************************************

# Pedir al usuario que ingrese el tipo (A o B) y el tamaño (1 o 2)
tipo = input("Ingrese el tipo de uva (A o B): ")
tamano = int(input("Ingrese el tamaño de la uva (1 o 2): "))

# Pedir al usuario que ingrese el precio inicial por kilo de uva
precio_inicial = float(input("Ingrese el precio inicial por kilo de uva: "))

# Calcular la ganancia según las reglas especificadas
ganancia = 0

if tipo == 'A':
    if tamano == 1:
        ganancia = precio_inicial + 0.20
    elif tamano == 2:
        ganancia = precio_inicial + 0.30
elif tipo == 'B':
    if tamano == 1:
        ganancia = precio_inicial - 0.30
    elif tamano == 2:
        ganancia = precio_inicial - 0.50

# Mostrar la ganancia obtenida
print("La ganancia obtenida es: " + str(ganancia) + " euros.")