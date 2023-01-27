# - Escribir una función que determine la longitud de la
# subcadena más larga que no contiene ninguna letra
# repetida.
from collections import Counter
def Contador(palabra):
    contador = Counter(palabra)
    repeticiones = [t[1] for t in list(contador.items()) if t[1] > 1]
    return len(repeticiones)  # devuelve si tiene repeticiones


def longitud(cadena):
    lista = cadena.split()
    print(lista)
    for i in lista:
        if Contador(i) == 0:
            return "tamaño de cadena :  "+ str(len(i)) + " valor de cadena : "+ str(i)

print(longitud("richard bruno huaman peralta"))