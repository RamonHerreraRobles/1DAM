#usuario: Ramon Herrera
#***********************************ENUNCIADO********************************
#Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos
#circunferencias y las clasifique en uno de estos estados:

#   - exteriores
#   - tangentes exteriores
#   - secantes
#   - tangentes interiores
#   - interiores
#   - concéntricas
#****************************************************************************

# Coordenadas y radios de las dos circunferencias
x1 = float(input("Ingrese la coordenada x1 de la primera circunferencia: "))
y1 = float(input("Ingrese la coordenada y1 de la primera circunferencia: "))
r1 = float(input("Ingrese el radio r1 de la primera circunferencia: "))

x2 = float(input("Ingrese la coordenada x2 de la segunda circunferencia: "))
y2 = float(input("Ingrese la coordenada y2 de la segunda circunferencia: "))
r2 = float(input("Ingrese el radio r2 de la segunda circunferencia: "))

# Distancias entre centros
d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
r = r1 + r2
R = abs(r1 - r2)

# Establecer el estado
if d > r:
    print("Las circunferencias se encuentran en estado: exteriores")
elif d == r:
    print("Las circunferencias se encuentran en estado: concéntricas")
elif d < R:
    print("Las circunferencias se encuentran en estado: interiores")
elif d == R:
    print("Las circunferencias se encuentran en estado: tangentes interiores")
elif R < d < r:
    print("Las circunferencias se encuentran en estado: secantes")
else:
    print("Las circunferencias se encuentran en estado: tangentes exteriores")