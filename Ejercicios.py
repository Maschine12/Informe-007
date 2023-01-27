# 5. EJERCICIOS:
# - Escribir una función que determine si una cadena es un
# palíndromo (se lee igual en ambos sentidos) o no:

from collections import Counter
import re

print("Ejercicio 1")


def palindromo(palabra):
    if palabra == palabra[::-1]:
        return "si es palindromo " + palabra
    else:
        return "No es palindromo" + palabra


print(palindromo("anitalavalatina"))

# - Escribir una función que determine la longitud de la
# subcadena más larga que no contiene ninguna letra
# repetida.

print("Ejercicio 2")


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


# - Escribir una función que divida una cadena dada en una
# lista de subcadenas cada vez que aparezca un carácter
# específico.

print("Ejercicio 3")


def separacion_caracter(cadena, caracter):
    cadena_separada = cadena.split(caracter)
    return cadena_separada


print(separacion_caracter("hola mi nombre es: Richard", ":"))

# - Escribir una función que determine la frecuencia de cada
# carácter en una cadena dada y devuelva un diccionario.
print("Ejercicio 4")


# - Escribir una función que determine la longitud de la
# subcadena más larga que contiene solo dígitos.

print("Ejercicio 5")


def subcadena_larga(palabra):
    subcadenas = palabra.split()
    lista_cadenas = []
    for i in subcadenas:
        lista_cadenas.append(len(i))
    for j in subcadenas:
        if len(j) == max(lista_cadenas):
            return str(i) + " de valor : " + str(len(j))


print("Valor de la cadena mas larga : "+subcadena_larga(
    "Hola soy Richard y este es un ejemplo de cadena busco la cadena masssss largaaaaaaa"))


# - Escribir una función que reemplace todas las apariciones
# de una subcadena en una cadena dada con otra subcadena
# dada.

print("Ejercicio 6")


def reemplazo_palabra(cadena, subcadena, subcadena_cambio):
    return re.sub(subcadena, subcadena_cambio, cadena)


pala = "En muchas partes del cuerpo como son las manos, las orejas o los pies, están representados todos los órganos y partes del cuerpo. Incidiendo sobre estas zonas se pueden crear arcos reflejos que actúen directamente sobre cualquier órgano del cuerpo y que solucionen cualgquier anomalía que exista.En las manos, las orejas o los pies, se representan todos los órganos del cuerpo. Incidiendo sobre estas zonas se pueden crear arcos reflejos que actúen directamente sobre cualquier punto del organismo y que solucionan cualquier punto del organismo y que solucionen la anomalía que exista."
subcadena = "las orejas o los pies"
subcadena_cambio = " orejas pies (cambio ¡¡¡¡)"
print(reemplazo_palabra(pala, subcadena, subcadena_cambio))
