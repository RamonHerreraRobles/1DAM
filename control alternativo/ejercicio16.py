##usuario: Ramon Herrera
#************************************ENUNCIADO********************************
#La política de cobro de una compañía telefónica es: cuando se realiza una 
#llamada, el cobro es por el tiempo que ésta dura, de tal forma que los primeros 
#cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos, los siguientes 
#dos minutos, 70 céntimos, y a partir del décimo minuto, 50 céntimos.
#Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, 
#en turno de mañana, 15 %, y en turno de tarde, 10 %. Realice un algoritmo para 
#determinar cuánto debe pagar por cada concepto una persona que realiza una llamada.
#****************************************************************************

tarifa_normal = [1, 0.8, 0.7, 0.5]

# Cargar las variables del programa
hora = int(input("Introduzca la hora (0-23): "))
minuto = int(input("Introduzca los minutos: "))

# Convertir los minutos a céntimos de euro
costo_total = int(minuto * 100 / 60) * 0.01

# Determinar el descuento de acuerdo al tiempo de la llamada
for i in range(len(tarifa_normal)):
    if costo_total <= i * 100 + 5000:
        descuento = tarifa_normal[i]
        break
    costo_total -= 5000

# Aplicar el descuento y calcular el costo final
costo_final = costo_total * descuento

# Calcular el impuesto
impuesto = costo_final * (3 if hora < 10 or hora >= 22 else (15 if hora < 17 else 10)) / 100

# Imprimir los resultados
print("El costo de la llamada es de", costo_final ,"euros.")
print("El impuesto es de", impuesto ,"euros.")
print("El costo total a pagar es de", costo_total + impuesto ,"euros.")