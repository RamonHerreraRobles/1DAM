#usuario: Ramon Herrera

#***********************************ENUNCIADO*********************************
#Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por 
#un alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las 
#notas, la nota media, la nota más alta que ha sacado y la menor.

lista_herrera=[]
seguir_herrera=False
menor_herrera=10
mayor_herrera=0
cont_herrera=0
media_herrera=0

for i in range(5):
    while seguir_herrera==False:
        nota_herrera=int(input("Introduce la "+str(i+1) +"ª nota: "))
        if (nota_herrera<0) or (nota_herrera>10):
            print("ERROR. INTRODUCE UN NUMERO ENTRE 0 Y 10")
        else:
            seguir_herrera=True
    if (nota_herrera<menor_herrera):
        menor_herrera=nota_herrera
    elif (nota_herrera>mayor_herrera):
        mayor_herrera=nota_herrera
    cont_herrera=cont_herrera+nota_herrera
    lista_herrera.append(nota_herrera)
    seguir_herrera=False

media_herrera=cont_herrera/5

print("Lista de notas:")
print(lista_herrera)
print("media:",media_herrera)
print("nota mas alta:",mayor_herrera)
print("nota mas baja:",menor_herrera)