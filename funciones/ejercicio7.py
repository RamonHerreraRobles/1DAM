#usuario: Ramon Herrera

#********************************ENUNCIADO************************
#Crear una subrutina llamada “Login”, que recibe un nombre de usuario 
#y una contraseña y te devuelve Verdadero si el nombre de usuario es 
#“usuario1” y la contraseña es “asdasd”. Además recibe el número de 
#intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.

#Crear un programa principal donde se pida un nombre de usuario y una 
#contraseña y se intente hacer login, solamente tenemos tres oportunidades para intentarlo.

from funciones import Login as login_herrera

usuario_herrera = input("Ingrese su nombre de usuario: ")
contraseña_herrera = input("Ingrese su contraseña: ")
intentos_herrera = 0

while intentos_herrera < 3:
    if login_herrera(usuario_herrera, contraseña_herrera, intentos_herrera):
        break
