#usuario: Ramon Herrera

#********************************ENUNCIADO************************
#Crea un función “ConvertirEspaciado”, que reciba como parámetro un 
#texto y devuelve una cadena con un espacio adicional tras cada letra. 
#Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa 
#principal donde se use dicha función.

from funciones import ConvertirEspaciado as espacio_herrera

texto_herrera = input("Ingrese un texto: ")

resultado_herrera = espacio_herrera(texto_herrera)
print("Texto convertido: ", resultado_herrera)
