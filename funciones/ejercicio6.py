#usuario: Ramon Herrera

#********************************ENUNCIADO************************
#Diseñar una función que calcule el área y el perímetro de una 
#circunferencia. Utiliza dicha función en un programa principal 
#que lea el radio de una circunferencia y muestre su área y perímetro.

from funciones import calcula_circunferencia as calculo_herrera

radio_herrera = float(input("Ingrese el radio de la circunferencia: "))
perimetro_herrera, area_herrera = calculo_herrera(radio_herrera)
print("El área de la circunferencia es: ", area_herrera)
print("El perímetro de la circunferencia es: ", perimetro_herrera)