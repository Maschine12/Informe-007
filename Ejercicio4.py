# - Escribir una función que determine la frecuencia de cada
# carácter en una cadena dada y devuelva un diccionario.
print("Ejercicio 4")
def Diccionario_texto(texto):
    retirar = ".;:.\n\"'"
    for i in retirar:
        texto = texto.replace(i,"")
    texto.lower()
    list_palabras = texto.split(" ")
    diccionario = {}
    for i in list_palabras:
        if i in diccionario:
            diccionario[i] += 1
        else:
            diccionario[i] = 1
    for j in diccionario:
        cantidad = diccionario[j]
        print(f"Palabra {j} se repite {cantidad}")
Diccionario_texto("La pulga y el piojo se quieren casar pero no se casan por falta de pan. Sale una hormiga de su hormigal: “Hagan las bodas, yo pongo el pan”. Pan ya tenemos. Pan ya tenemos. Ahora el vino, ¿dónde lo hallaremos? Sale un mosquito detrás de un pino: “Hagan las bodas, yo pongo el vino”. Vino tenemos. Vino tenemos. Ahora la carne, ¿dónde la hallaremos? Sale un lobo de su lobera: “Hagan las bodas, yo pongo ternera”. Carne tenemos. Carne tenemos. Y ahora la madrina, ¿dónde la hallaremos? Sale una rata de la cocina: “Hagan las bodas, yo seré madrina”. Madrina tenemos. Madrina tenemos. Y ahora el padrino, ¿dónde lo hallaremos? Sale un ratón detrás de un molino: “Hagan las bodas, yo seré el padrino”. Estando en la boda bebiéndose el vino llegó un gato negro y se llevó al padrino.")
