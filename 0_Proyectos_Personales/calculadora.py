def calculadora(*args):
    print(f"El resultado de su operacion es: {eval(args[0])}")

def main():
    operacion = input("Ingrese su operacion: ")
    calculadora(operacion)
        
if __name__ == "__main__":
    main()
