#usuario: Ramon Herrera

#*****************************ENUNCIADO***********************************
#Realizar un programa que compruebe si una cadena contiene una subcadena. 
#Las dos cadenas se introducen por teclado.

cadena_herrera=input("Introduzca una cadena de una o mas palabras: ")

subcadena_herrera=input("Introduzca una subcadena: ")
if ( subcadena_herrera in cadena_herrera):
    print ("La cadena '"+cadena_herrera+"' contiene la subcadena '"+subcadena_herrera+"'")
else:
    print ("La cadena '"+cadena_herrera+"' no contiene la subcadena '"+subcadena_herrera+"'")