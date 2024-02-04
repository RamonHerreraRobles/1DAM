#usuario: Ramon Herrera

#*****************************ENUNCIADO***********************************
#Pide una cadena y un carácter por teclado (valida que sea un carácter) y 
#muestra cuantas veces aparece el carácter en la cadena.

adelante_herrera=False
cadena_herrera=input("Introduce una cadena:")
while adelante_herrera==False:
    letra_herrera=input("Introduce una letra para comprobar cuantas veces aparece en la cadena:")
    if not letra_herrera.isalpha():
        print ("No es una letra, vuelve a introducirla.")
    elif len(letra_herrera)>1:
        print ("No es una sola letra, vuelve a introducir.")
    else:
        adelante_herrera=True

cont_herrera=0
for caracter_herrera in cadena_herrera:
    if caracter_herrera==letra_herrera:
        cont_herrera+=1

print("la cadena '"+letra_herrera+"' aparece",cont_herrera,"veces")