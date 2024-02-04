#usuario: Ramon Herrera

#*********************************ENUNCIADO***************************
#Escribe un programa que pida el limite inferior y superior de un intervalo. 
#Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
#A continuación se van introduciendo números hasta que introduzcamos el 0. 
#Cuando termine el programa dará las siguientes informaciones:

#   -La suma de los números que están dentro del intervalo (intervalo abierto).
#   -Cuantos números están fuera del intervalo.
#   -He informa si hemos introducido algún número igual a los límites del intervalo.Realizar una algoritmo que muestre la tabla de multiplicar de un número introducido por teclado.
#*********************************************************************

igual_herrera=False
cont_herrera = 0 
fuera_herrera=0
prim_herrera=int(input("Escribe un numero:"))
ult_herrera=int(input("Escribe otro numero:"))

if (prim_herrera>ult_herrera):
    print("El segundo numero no puede ser menor que el primero")
    prim_herrera=int(input("Escribe un numero:"))
    ult_herrera=int(input("Escribe otro numero:"))

num_herrera=1
while num_herrera != 0:
    num_herrera=int(input("Escribe un numero:"))
    if (num_herrera>prim_herrera) and (num_herrera<ult_herrera):
        cont_herrera=cont_herrera+num_herrera
    else:
        if (num_herrera==prim_herrera) or (num_herrera==ult_herrera):
            igual_herrera=True
        else:
            fuera_herrera=fuera_herrera+1
    
#pongo esta conversion ya que al añadir 0 en el bucle, se suma a uno de los contadores
if (prim_herrera>0):
    fuera_herrera=fuera_herrera-1

print ("Suma de numeros en el rango", cont_herrera,)
print ("Numeros fuera del rango: ", fuera_herrera, "numeros")
if (igual_herrera==True):
    print ("Se ha introducido un numero igual a los limites del intervalo")
else:
    print ("No se ha introducido ningun numero igual a los intervalos")