#usuario: Ramon Herrera

#*******************************ENUNCIADO****************************
#Hacer un programa que muestre un cronometro, indicando las horas, minutos y segundos.

import time

while True:
    momento_herrera = time.localtime()
    hora_herrera = time.strftime("%H:%M:%S", momento_herrera)
    print(hora_herrera)
    time.sleep(1)