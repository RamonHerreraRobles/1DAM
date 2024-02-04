#usuario: Ramon Herrera

#******************************ENUNCIADO********************************
#Escribe un programa python que pida un número por teclado y que cree un 
#diccionario cuyas claves sean desde el número 1 hasta el número indicado, 
#y los valores sean los cuadrados de las claves.

num_herrera = int(input("Introduce un número: "))
diccionario_herrera = {i: i**2 for i in range(1, num_herrera+1)}
print(diccionario_herrera)