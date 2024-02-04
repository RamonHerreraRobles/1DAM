#usuario: Ramon Herrera

#*******************************ENUNCIADO****************************
# Realizar un ejemplo de menú, donde podemos escoger las distintas opciones hasta que seleccionamos la opción de “Salir”

salir_herrera=False

while salir_herrera==False:
    print("MENUS")
    print("Elige el menú que prefieras o seleccione la opcion de 'Salir'")
    print("1. Menú italiano")
    print("2. Menú español")
    print("3. Menú americano")
    print("4. Salir")
    menu_herrera = input("Ingrese su elección: ")
    if menu_herrera == "1":
        print ("Menú italiano")
        print ("Pizza margherita con salsa de tomate y queso mozzarella.")
        print ("Pollo al ajillo acompañado de patatas fritas.")
        print ("Ensalada de espinacas, tomates cherry y aguacate.")
        print ("Bocadillo de pan integral relleno de carne de cerdo y queso parmesano.")
    elif menu_herrera == "2":
        print ("Menú español")
        print ("Tortilla española con huevo duro y cebolla roja.")
        print ("Cordero asado con patatas y ensalada verde.")
        print ("Lentejas con garbanzos y pepino en aceite de oliva.")
        print ("Pan con tomate y jamón ibérico.")
    elif menu_herrera == "3":
        print ("Menú americano")
        print ("Hamburguesa de pollo con bacon, lechuga, tomate, mayonesa y mostaza.")
        print ("Hot dog con ketchup, mustard y aguacate.")
        print ("Sándwich de pavo a la plancha con champiñones, tocino, lechuga, tomate y mayonesa")
        print ("Fries con salsa de soya.")
    elif menu_herrera == "Salir":
        salir_herrera=True
    else:
        print ("Opción no válida. Por favor ingrese una opción del 1 al 3 o 'Salir'.")