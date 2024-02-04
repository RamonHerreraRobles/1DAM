#usuario: Ramon Herrera

#*******************************ENUNCIADO****************************
#Escribe un programa que dados dos números, uno real (base) y un entero 
#positivo (exponente), saque por pantalla el resultado de la potencia. 
#No se puede utilizar el operador de potencia.


seguir=False

while not seguir:

    base_herrera = int(input("Introduce un numero para la base:"))
    exponente_herrera = int(input("Introduce un numero para el exponente:"))

    if (base_herrera>=0) and (exponente_herrera>=0):
        seguir=True
    else:
        print ("Error, los numeros no pueden ser negativos")



resultado_herrera = 1

for i in range(exponente_herrera):
    if (exponente_herrera==0):
        resultado_herrera = 1
    else:
        if (exponente_herrera==1):
            resultado_herrera = base_herrera
        else:
            resultado_herrera = resultado_herrera * base_herrera


print(resultado_herrera)