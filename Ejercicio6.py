# - Escribir una función que reemplace todas las apariciones
# de una subcadena en una cadena dada con otra subcadena
# dada.
import re
print("Ejercicio 6")


def reemplazo_palabra(cadena, subcadena, subcadena_cambio):
    return re.sub(subcadena, subcadena_cambio, cadena)


pala = "En muchas partes del cuerpo como son las manos, las orejas o los pies, están representados todos los órganos y partes del cuerpo. Incidiendo sobre estas zonas se pueden crear arcos reflejos que actúen directamente sobre cualquier órgano del cuerpo y que solucionen cualgquier anomalía que exista.En las manos, las orejas o los pies, se representan todos los órganos del cuerpo. Incidiendo sobre estas zonas se pueden crear arcos reflejos que actúen directamente sobre cualquier punto del organismo y que solucionan cualquier punto del organismo y que solucionen la anomalía que exista."
subcadena = "las orejas o los pies"
subcadena_cambio = " orejas pies (cambio ¡¡¡¡)"
print(reemplazo_palabra(pala, subcadena, subcadena_cambio))
