#usuario: Ramon Herrera

#***********************************ENUNCIADO*********************************
#Programa que declare una lista y la vaya llenando de números hasta que 
#introduzcamos un número negativo. Entonces se debe imprimir el vector 
#(sólo los elementos introducidos).

lista_herrera=[]
seguir_herrera=False

print("Introduce numeros (numero negativo para terminar):")
while seguir_herrera==False:
    num_herrera=int(input(""))
    if (num_herrera>=0):
        lista_herrera.append(num_herrera)
    else:
        seguir_herrera=True

print(lista_herrera)