#usuario: Ramon Herrera

#*********************************ENUNCIADO***************************
#Realizar una algoritmo que muestre la tabla de multiplicar de un número introducido por teclado.
#*********************************************************************

num_herrera=int(input("Escribe un numero:"))
print ("Tabla del", num_herrera)

for mult_herrera in range (1,11):
    print (mult_herrera,"x", num_herrera ,"=" , mult_herrera * num_herrera )
    