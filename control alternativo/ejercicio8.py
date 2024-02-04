#usuario: Ramon Herrera
#*****************************************ENUNCIADO*****************************************
#Algoritmo que pida dos números ‘nota’ y ‘edad’ y un carácter ‘sexo’ y muestre el mensaje 
#‘ACEPTADA’ si la nota es mayor o igual a cinco, la edad es mayor o igual a dieciocho y el 
#sexo es ‘F’. En caso de que se cumpla lo mismo, pero el sexo sea ‘M’, debe imprimir ‘POSIBLE’. 
#Si no se cumplen dichas condiciones se debe mostrar ‘NO ACEPTADA’.
#*****************************************************************************************

# Solicitar dos números por teclado
nota = float(input("Ingrese la nota: "))
edad = int(input("Ingrese la edad: "))

# Solicitar un carácter por teclado
sexo = input("Ingrese el sexo (F/M): ")
sexo = sexo.upper()

# Crear un condicional que verifique las condiciones para mostrar el mensaje 'ACEPTADA', 'POSIBLE' o 'NO ACEPTADA'
if nota >= 5 and edad >= 18 and sexo == 'F':
    print("ACEPTADA")
elif nota >= 5 and edad >= 18 and sexo == 'M':
    print("POSIBLE")
else:
    print("NO ACEPTADA")