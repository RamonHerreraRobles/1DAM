#usuario: Ramon herrera
#********************************ENUNCIADO********************************
#Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las 
#dimensiones  de los lados de un triángulo. El programa debe determinar que 
#tipo de triangulo es, teniendo en cuenta los siguiente:

#- Si se cumple Pitágoras entonces es triángulo rectángulo
#- Si sólo dos lados del triángulo son iguales entonces es isósceles.
#- Si los 3 lados son iguales entonces es equilátero.
#- Si no se cumple ninguna de las condiciones anteriores, es escaleno.
#***********************************************************************

import math

print("Ingrese la longitud del lado A:")
A = float(input())

print("Ingrese la longitud del lado B:")
B = float(input())

print("Ingrese la longitud del lado C:")
C = float(input())

# Comprobar si se cumple Pitágoras
if math.isclose(A**2 + B**2, C**2, rel_tol=1e-5) or math.isclose(B**2 + C**2, A**2, rel_tol=1e-5) or math.isclose(C**2 + A**2, B**2, rel_tol=1e-5):
    if A**2+B**2 == C**2:
        print("El triángulo es rectángulo.")

# Comprobar si el triángulo es equilátero
elif A == B == C:
    print("El triángulo es equilátero.")
    
# Comprobar si el triángulo es isósceles
elif A == B or B == C or C == A:
    print("El triángulo es isósceles.")

# Si no se cumple ninguna de las condiciones anteriores, el triángulo es escaleno
else:
    print("El triángulo es escaleno.")