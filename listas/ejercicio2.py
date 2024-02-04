#usuario: Ramon Herrera

#***********************************ENUNCIADO*********************************
#Crea una lista e inicialízala con 5 cadenas de caracteres leídas por teclado. 
#Copia los elementos de la lista en otra lista pero en orden inverso, y muestra 
#sus elementos por la pantalla.

lista_herrera=[]

for i in range (5):
    cad_herrera=input("Introduce una cadena: ")
    lista_herrera.append(cad_herrera)

inversa_herrera=lista_herrera[::-1]

print("Elemenos de la lista inversa: ")
print(inversa_herrera)