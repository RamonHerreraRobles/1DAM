#usuario: Ramon Herrera

#***********************************ENUNCIADO*********************************
#Crea un programa que pida un número al usuario un número de mes 
#(por ejemplo, el 4) y diga cuántos días tiene (por ejemplo, 30) y el nombre 
#del mes. Debes usar listas. Para simplificarlo vamos a suponer que febrero tiene 28 días.

n_dias_herrera = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
meses_herrera=["enero", "febrero","marzo",  "abril", "mayo", "junio", "julio", "agosto","septiembre", "octubre", "noviembre", "diciembre"]


seguir_herrera=False

print("Introduce un numero entre 1 y 12:")
while seguir_herrera==False:
    num_herrera=int(input(""))
    if (num_herrera>=1) and (num_herrera<=12):
        seguir_herrera=True
    else: 
        print("ERROR. INTRODUCE UN NUMERO ENTRE 1 Y 12")

dia_herrera=n_dias_herrera[num_herrera-1]
nombre_herrera=meses_herrera[num_herrera-1].capitalize()

print(nombre_herrera,"tiene",dia_herrera,"dias")