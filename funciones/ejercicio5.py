#usuario: Ramon Herrera

#********************************ENUNCIADO************************
#Crea una función “calcularMaxMin” que recibe una lista con valores 
#numéricos y devuelve el valor máximo y el mínimo. Crea un programa 
#que pida números por teclado y muestre el máximo y el mínimo, 
#utilizando la función anterior.

from funciones import calcularMaxMin as MaxMin_herrera

try:
    lista_herrera = []
    while True:
        n = float(input("Introduzca un número (pulse la tecla 'Intro' para terminar): "))
        lista_herrera.append(n)
except ValueError:
    print("Lista de numeros cerrada")

try:
    maxymin_herrera = MaxMin_herrera(lista_herrera)
    print(f"El valor máximo es: {maxymin_herrera[0]}")
    print(f"El valor mínimo es: {maxymin_herrera[1]}")
except ZeroDivisionError:
    print("No se puede realizar la operación debido a la lista de valores numéricos")
except IndexError:
    print("La lista está vacía. No se puede realizar la operación")