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
