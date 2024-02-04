#usuario: Ramon Herrrera
#********************************************ENUNCIADO************************************
#Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);
#*****************************************************************************************

# Se piden los numeros 
print("Ingrese el primer número:")
number1 = int(input())
print("Ingrese el segundo número:")
number2 = int(input())
print("Ingrese el tercer número:")
number3 = int(input())

#dependiendo los numeros, se ordenan
if number1 >= number2:
    if number1 >= number3:
        print("Los números ordenados (de mayor a menor) son:", number1, number2, number3)
    else:
        print("Los números ordenados (de mayor a menor) son:", number3, number1, number2)
else:
    if number2 >= number3:
        print("Los números ordenados (de mayor a menor) son:", number2, number3, number1)
    else:
        print("Los números ordenados (de mayor a menor) son:", number3, number2, number1)