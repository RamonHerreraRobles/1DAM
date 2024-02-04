#usuario: Ramon Herrera

#*****************************ENUNCIADO***********************************
#Pide una cadena y dos caracteres por teclado (valida que sea un carácter), 
#sustituye la aparición del primer carácter en la cadena por el segundo carácter.

seguir1_herrera=False
seguir2_herrera=False

cadena_herrera=input("Introduce una cadena: ")

while seguir1_herrera==False:
    letra1_herrera=input("Introduce una letra que será sustituida:")
    if len(letra1_herrera)!=1:
        print ("Error, introduzca solo una letra.")
    else:
        seguir1_herrera=True

while seguir2_herrera==False:
    letra2_herrera=input("Introduce otra letra para sustituirla: ")
    if len(letra2_herrera)!=1:
        print ("Error, introduzca solo una letra.")
    else:
        seguir2_herrera=True

sustitucion_herrera=cadena_herrera.replace(letra1_herrera,letra2_herrera)

print(sustitucion_herrera)