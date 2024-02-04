#usuario: Ramon Herrera

#********************************ENUNCIADO************************
#Crea un programa que pida dos número enteros al usuario y diga si 
#alguno de ellos es múltiplo del otro. Crea una función EsMultiplo 
#que reciba los dos números, y devuelve si el primero es múltiplo del segundo.

n1_hererra = int(input("Ingrese el primer número: "))
n2_herrera = int(input("Ingrese el segundo número: "))

from funciones import EsMultiplo as mul_herrera

if mul_herrera(n1_hererra, n2_herrera):
    print(f"{n1_hererra} es múltiplo de {n2_herrera}")
elif mul_herrera(n2_herrera, n1_hererra):
    print(f"{n2_herrera} es múltiplo de {n1_hererra}")
else:
    print("Ninguno de los dos números es múltiplo del otro")