# - Escribir una función que divida una cadena dada en una
# lista de subcadenas cada vez que aparezca un carácter
# específico.
print("Ejercicio 3")

def separacion_caracter(cadena, caracter):
    cadena_separada = cadena.split(caracter)
    return cadena_separada

print(separacion_caracter("hola mi nombre es: Richard", ":"))