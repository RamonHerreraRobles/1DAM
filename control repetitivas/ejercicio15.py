#usuario: Ramon Herrera

#*******************************ENUNCIADO****************************
#Una persona adquirió un producto para pagar en 20 meses. El primer mes 
#pagó 10 €, el segundo 20 €, el tercero 40 € y así sucesivamente. 
#Realizar un algoritmo para determinar cuánto debe pagar mensualmente y 
#el total de lo que pagó después de los 20 meses.

pago_herrera=10
meses_herrera=1
total_herrera=0

while meses_herrera<=20:
    print("En el mes",meses_herrera,"pagara:")
    if (meses_herrera==1):
        print(pago_herrera,"euros")
    else:
        pago_herrera=pago_herrera+pago_herrera
        print(pago_herrera,"euros")
        total_herrera=total_herrera+pago_herrera

    meses_herrera=meses_herrera+1

print("El total a pagar es de",total_herrera)