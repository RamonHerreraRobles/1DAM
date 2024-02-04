#funcion ejercicio 1
#Esta funcion recibe el texto escrito en el ejercicio 1 ,y lo escribe centrado a la pantalla y lo subraya
def EscribirCentrado(texto_herrera):
    centro_herrera = 40 - len(texto_herrera) // 2
    subrayar_herrera = '=' * len(texto_herrera)

    print("\n".join(
        [" " * centro_herrera + texto_herrera + " " * centro_herrera,
         " " * centro_herrera + subrayar_herrera + " " * centro_herrera]
    ))

#funcion ejercicio 2
#Esta funcion se dedica a recibir los dos numeros introducidos por teclado y comprueban si son multiplos 
#comprobando que la resta de la division entre ellos es igual a 0
def EsMultiplo(a, b):
    return a % b == 0

#funcion ejercicio 3
#Esta funcion se encarga de hacer la media entre la temperatura maxima y la minima de cada dia
def calcular_temperatura_media(max_herrera, min_herrera):
    return (max_herrera + min_herrera) / 2

#funcion ejercicio 4
#Esta funcion se dedica a recibir una cadena y separar cada caracter con espacios
def ConvertirEspaciado(texto_herrera):
    return " ".join(texto_herrera)

#funcion ejercicio 5
#Esta funcion lee los numeros introducidos en una lista y van comparando para determinar cual es el 
#maximo y cual el minimo
def calcularMaxMin(lista_herrera):
    maximo_herrera = minimo_herrera = lista_herrera[0]
    for i in lista_herrera:
        if i > maximo_herrera:
            maximo_herrera = i
        elif i < minimo_herrera:
            minimo_herrera = i
    return maximo_herrera, minimo_herrera

#funcion ejercicio 6
#Esta funcion hace varios calculos e imprime los resultados en el programa 'ejercicio6'
import math
def calcula_circunferencia(radio_herrera):
    diametro_herrera = radio_herrera * 2
    perimetro_herrera = diametro_herrera * math.pi
    area_herrera = math.pi * (radio_herrera ** 2)
    return perimetro_herrera, area_herrera


#funcion ejercicio 7
def Login(usuario_herrera, contraseña_herrera, intentos_herrera):
    if usuario_herrera == "usuario1" and contraseña_herrera == "asdasd":
        print("Inicio de sesión exitoso")
        return True
    else:
        print("Intentos de inicio de sesión restantes: ", 3 - intentos_herrera)
        intentos_herrera += 1
        if intentos_herrera == 3:
            print("Se ha alcanzado el límite de intentos. Intente de nuevo más tarde.")
            return False
        return False


#funcion ejercicio 8
#Esta funcion lee un numero introducido en el programa y calcula su factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
#funcion ejercicio 9
def mcd(a, b):
    while(b):
        a, b = b, a % b
    return a

#funciones ejercicio 10
def segundos_a_horas_minutos_segundos(segundos_herrera):
    horas_herrera = segundos_herrera // 3600
    minutos_herrera = (segundos_herrera % 3600) // 60
    segundos_herrera = (segundos_herrera % 3600) % 60
    return horas_herrera, minutos_herrera, segundos_herrera

def horas_minutos_segundos_a_segundos(horas_herrera, minutos_herrera, segundos_herrera):
    segundos_herrera = horas_herrera * 3600 + minutos_herrera * 60 + segundos_herrera
    return segundos_herrera

#funciones ejercicio 11
def LeerFecha():
    dia_herrera = int(input("Día: "))
    mes_herrera = int(input("Mes: "))
    anyo_herrera = int(input("Año: "))
    return dia_herrera, mes_herrera, anyo_herrera

def DiasDelMes(mes_herrera, anyo_herrera):
    if mes_herrera == 2:
        if EsBisiesto(anyo_herrera):
            return 29
        else:
            return 28
    elif mes_herrera in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def EsBisiesto(anyo_herrera):
    if anyo_herrera % 4 == 0:
        if anyo_herrera % 100 == 0:
            if anyo_herrera % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def Calcular_Dia_Juliano(dia_herrera, mes_herrera, anyo_herrera):
    if mes_herrera < 3:
        mes_herrera += 12
        anyo_herrera -= 1
    return dia_herrera + int((13 * (mes_herrera + 1)) / 5) + anyo_herrera + anyo_herrera / 4 - anyo_herrera / 100 + anyo_herrera / 400 - 32083

#funcion ejercicio 12
def Valido(dia_herrera, mes_herrera, anyo_herrera):
    if dia_herrera > DiasDelMes(mes_herrera, anyo_herrera) or dia_herrera < 1 or mes_herrera > 12 or mes_herrera < 1 or anyo_herrera < 1:
        return False
    return True