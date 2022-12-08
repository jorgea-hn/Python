def conversor(valor_dolar, pais):
    cantidad_moneda = float(input(f"Ingrese cantidad de {pais}: "))

    dolares = cantidad_moneda / valor_dolar
    dolares = round(dolares,2)

    print(f"Tienes ${dolares} Dolares")


def main():

    while True:
        menu = """
        1 - Soles Peruanos a Dolares
        2 - Pesos Mexicanos a Dolares
        3 - Pesos Colombianos a Dolares
        4 - Salir
        Ingrese una opcion
        """
        opcion = input(menu)

        if opcion == "1":
            conversor(3.61,"Soles Peruanos")
        elif opcion == "2":
            conversor(20,"Pesos Mexicanos")
        elif opcion =="3":
            conversor(3471.27,"Pesos Colombianos")
        elif opcion == "4":
            print("Cerrando conversor de monedas ")
            break
        else:
            print("Opcion incorrecta")
            print("Vuelva a ingresar una opcion correcta")

if __name__ == "__main__":
    main()
