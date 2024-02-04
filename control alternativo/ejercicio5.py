#usuario: Ramon Herrera
#*********************************ENUNCIADO*********************************
#Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.
#***************************************************************************

print("Ingrese un nombre de usuario:")
nombre_usuario = input()

print("Ingrese una contraseña:")
contraseña = input()

if nombre_usuario == "pepe" and contraseña == "asdasd":
    print("Has entrado al sistema.")
else:
    print("Error: nombre de usuario o contraseña incorrecta.")