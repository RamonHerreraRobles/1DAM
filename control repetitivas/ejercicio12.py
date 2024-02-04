#usuario: Ramon Herrera

#*******************************ENUNCIADO****************************
#Realizar un algoritmo para determinar cuánto ahorrará una persona en 
#un año, si al final de cada mes deposita cantidades variables de dinero; 
#además, se quiere saber cuánto lleva ahorrado cada mes.


ahorro_mes_herrera = 0
ahorro_anual_herrera = 0
mes_herrera = 1

while mes_herrera <= 12:
    print("Mes ", mes_herrera)
    cantidad_herrera = float(input("Ingrese la cantidad de dinero que desea depositar en el mes: "))


    ahorro_mes_herrera = cantidad_herrera
    ahorro_anual_herrera =ahorro_anual_herrera + ahorro_mes_herrera

    print("Al final del mes", mes_herrera , ", se ha ahorrado", ahorro_mes_herrera ,"euros")


    mes_herrera=mes_herrera+1

print("Al final del año, ha ahorrado un total de", ahorro_anual_herrera, "euros")