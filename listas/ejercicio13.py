#usuario:Ramon Herrera

#************************************ENUNCIADO*******************************
#De una empresa de transporte se quiere guardar el nombre de los conductores que ç
#tiene, y los kilómetros que conducen cada día de la semana.

#Para guardar esta información se van a utilizar dos arreglos:

#Nombre: Lista para guardar los nombres de los conductores.
#kms: Tabla para guardar los kilómetros que realizan cada día de la semana.
#Se quiere generar una nueva lista (“total_kms”) con los kilómetros totales que realza cada conductor.

#Al finalizar se muestra la lista con los nombres de conductores y los kilómetros que ha realizado.

nombre_herrera = []
kms_herrera = []
dia_herrera=["lunes","martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

num_conductores_herrera = int(input("Ingrese el número de conductores: "))

for i in range(num_conductores_herrera):
    conductor_herrera = input("Ingrese el nombre del conductor " + str(i+1) + ": ")
    nombre_herrera.append(conductor_herrera)
    
    km_dias_herrera = []
    for j in range(7):
        km_herrera = float(input("Introduzca el numero de kilómetros que ha recorrido " + conductor_herrera + " el " + dia_herrera[j] + ": "))
        km_dias_herrera.append(km_herrera)

    
    kms_herrera.append(km_dias_herrera)

total_kms_herrera = []
for i in range(num_conductores_herrera):
    suma_kms_herrera = sum(kms_herrera[i])
    total_kms_herrera.append(suma_kms_herrera)

for i in range(num_conductores_herrera):
    print("Conductor: ", nombre_herrera[i], " - Kilómetros totales: ", total_kms_herrera[i])