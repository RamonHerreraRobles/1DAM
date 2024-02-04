#usuario: Ramon Herrera

#*****************************ENUNCIADO***********************************
#Realizar un programa que comprueba si una cadena leída por teclado comienza 
#por una subcadena introducida por teclado.

cadena_herrera=input("Introduzca una cadena de una o mas palabras:")

subcadena_herrera=input("Introduzca una subcadena:")
if (cadena_herrera.startswith (subcadena_herrera)):
    print ("La cadena '"+cadena_herrera+"' comienza con la subcadena '"+subcadena_herrera+"'")
else:
    print ("La cadena '"+cadena_herrera+"' no comienza con la subcadena '"+subcadena_herrera+"'")