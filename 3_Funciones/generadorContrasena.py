import random
import string

def generar_contrasena():
    minusculas = list(string.ascii_lowercase)
    mayusculas = list(string.ascii_uppercase)
    simbolos = ["#","$","%","&"]
    numeros = ["1","2","3","4","5","6","7","8","9","0"]

    caracteres = mayusculas + minusculas + simbolos + numeros

    contrasena = []
    for i in range (0,15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena  = "".join(contrasena)
    return contrasena


def main():
    contrasena = generar_contrasena()
    print("Tu nueva contrasena es: ", contrasena)

if __name__ == "__main__":
    main()

