#Ejercicio 1

# -----Palabra palindromo
"""def palindromo(palabra):
    if palabra == palabra[::-1]:
        print("Palabra palindroma")
    else:
        print("Palabra no palindroma")

palabra = input("Ingrese una palabra: ")
palindromo(palabra)"""


def palindromo(palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()

    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False

#Funcion principal
def main():
    palabra = input("Ingrese una palabra: ")
    es_palindomo = palindromo(palabra)

    if es_palindomo:
        print("Es palindromo")
    else:
        print("No es palindromo")


#Punto de la entrada de la aplicacion
if __name__ == "__main__":
    main()


