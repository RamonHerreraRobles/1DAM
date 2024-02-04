#usuario: Ramon Herrera

#*******************************ENUNCIADO****************************
#Mostrar en pantalla los N primero número primos. Se pide por teclado 
#la cantidad de números primos que queremos mostrar.

cantidad_primos_herrera = int(input("Ingrese la cantidad de números primos que desea mostrar: "))
if cantidad_primos_herrera <= 0:
    print("Por favor, ingrese un número entero positivo mayor que cero.")
else:
    primos_herrera = []
    numero_herrera = 2
    while len(primos_herrera) < cantidad_primos_herrera:
        es_primo = True
        #Copio esta estructura del ejercicio 11
        for i in range(2, int(numero_herrera ** 0.5) + 1):
            if numero_herrera % i == 0:
                es_primo = False
                break
        if es_primo:
            primos_herrera.append(numero_herrera)
        numero_herrera += 1

    print("Los primeros ", cantidad_primos_herrera ,"números primos son:", primos_herrera)