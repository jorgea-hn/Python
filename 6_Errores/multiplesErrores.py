
divi=0
try:
    a = int(input("Ingrese el dividendo: "))
    b = int(input("Ingrese el divisor: "))
    divi = a/b
except ValueError:
    print("Error: Solo ingrese numeros enteros")
except ZeroDivisionError:
    print("Error: No se puede dividir entre 0")
except Exception as error:
    print("Ha ocurrido error no previsto: ", type(error).__name__)

print("La division es: ", divi)