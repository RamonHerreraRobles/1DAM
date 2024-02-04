#usuario: Ramon Herrera

#***************************************ENUNCIADO*******************************
#Queremos guardar la temperatura mínima y máxima de 5 días. Realiza un programa 
#que de la siguiente información:

#-La temperatura media de cada día
#-Los días con menos temperatura
#-Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima 
#coincide con ella. si no existe ningún día se muestra un mensaje de información.
#*********************************************************************************

temperaturas_herrera = []

semana_herrera = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

for i in range(5):
    temp_herrera = int(input(f"Ingrese la temperatura del día {i+1}: "))
    temperaturas_herrera.append(temp_herrera)

temp_minima_herrera = min(temperaturas_herrera)
temp_maxima_herrera = max(temperaturas_herrera)
temp_media_herrera = sum(temperaturas_herrera) / len(temperaturas_herrera)

print("Temperatura media de cada día:", temp_media_herrera)
print("Temperatura mínima:", temp_minima_herrera)
print("Temperatura máxima:", temp_maxima_herrera)

dias_minima_herrera = [semana_herrera[i] for i, temp in enumerate(temperaturas_herrera) if temp == temp_minima_herrera]
print("Los días con menos temperatura que la máxima son:", dias_minima_herrera)

temp_usuario_herrera = int(input("Ingrese una temperatura: "))
dia_maxima_usuario_herrera = [semana_herrera[i] for i, temp_herrera in enumerate(temperaturas_herrera) if temp_herrera == temp_usuario_herrera]
if dia_maxima_usuario_herrera:
    print("Los días cuya temperatura máxima coincide con la ingresada son:", dia_maxima_usuario_herrera)
else:
    print("No existe ningún día cuya temperatura máxima coincide con la ingresada.")