import my_paquete.aritmetica as a 

def main():
    suma = a.sumar(4,4,5,8,9)
    resta = a.restar(10,5)
    potencia = a.potenciar(3,3)

    print("La suma es: ",suma)
    print("La resta es: ", resta)
    print("La potencia es: ", potencia)

if __name__ == "__main__":
    main()