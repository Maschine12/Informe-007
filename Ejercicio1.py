# 5. EJERCICIOS:
# - Escribir una función que determine si una cadena es un
# palíndromo (se lee igual en ambos sentidos) o no:

print("Ejercicio 1")


def palindromo(palabra):
    if palabra == palabra[::-1]:
        return "si es palindromo " + palabra
    else:
        return "No es palindromo" + palabra
        
print(palindromo("anitalavalatina"))