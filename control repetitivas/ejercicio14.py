#usuario: Ramon Herrera

#*******************************ENUNCIADO****************************
#Una persona se encuentra en el kilómetro 70 de una carretera, otra se 
#encuentra en el km 150, los coches tienen sentido opuesto y tienen la 
#misma velocidad. Realizar un programa para determinar en qué kilómetro 
#de esa carretera se encontrarán.


persona1_herrera = 70
persona2_herrera = 150
velocidad_herrera= int(input("Introduce la velocidad a la q van los coches(km/h):"))


distancia_herrera = (persona2_herrera - persona1_herrera)/2

tiempo_herrera = distancia_herrera / velocidad_herrera

encuentro_herrera = persona1_herrera + velocidad_herrera* tiempo_herrera

print("Se encontraran en el kilometro",encuentro_herrera)