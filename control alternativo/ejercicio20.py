##usuario: Ramon Herrera
#************************************ENUNCIADO********************************
#Una compañía de transporte internacional tiene servicio en algunos países de 
#América del Norte, América Central, América del Sur, Europa y Asia. El costo 
#por el servicio de transporte se basa en el peso del paquete y la zona a la 
#que va dirigido. Lo anterior se muestra en la tabla:

#Zona	Ubicación	Costo/gramo
#1	América del Norte	24.00 euros
#2	América Central	20.00 euros
#3	América del Sur	21.00 euros
#4	Europa	10.00 euros
#5	Asia	18.00 euros
#Parte de su política implica que los paquetes con un peso superior a 5 kg no 
#son transportados, esto por cuestiones de logística y de seguridad.
#Realice un algoritmo para determinar el cobro por la entrega de un paquete o, 
#en su caso, el rechazo de la entrega.
#****************************************************************************

print("America del Norte:1")
print("America Central:2")
print("America del Sur:3")
print("Europa:4")
print("Asia:5")
ubicacion = input("Ingrese el número de la ubicación (1-5): ")
peso = float(input("Ingrese el peso del paquete en kg: "))

if ubicacion == '1':
    zona = 1
    costo_kg = 24.00
elif ubicacion == '2':
    zona = 2
    costo_kg = 20.00
elif ubicacion == '3':
    zona = 3
    costo_kg = 21.00
elif ubicacion == '4':
    zona = 4
    costo_kg = 10.00
elif ubicacion == '5':
    zona = 5
    costo_kg = 18.00
else:
    print("Ubicación no válida.")

if peso > 5:
    print("El paquete no será transportado, el peso excede el límite de 5 kg.")
else:
    costo_total = peso * costo_kg
    print("El costo por la entrega del paquete es de:", costo_total, "euros.")