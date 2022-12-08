from figuras import Circulo,Rectangulo,probarFigura

def main():
    while True:
        menu = """
        AREA Y PERIMETRO DE FIGURAS GEOMETRICAS
        1 - Rectangulo
        2 - Circulo
        3 - Salir
        INGRESE SU OPCION: """
        opcion = input(menu)

        if opcion=="1":
            print("opcion1 ---- Rectangulo ")
            base = float(input("Ingrese el valor de la base: "))
            altura = float(input("Ingrese el valor de la altura: "))
            rect1 = Rectangulo(base,altura)
            probarFigura(rect1)
        elif opcion=="2":
            print("opcion2 ---- Circulo ")
            radio = float(input("Ingrese el valor del radio: "))
            c1 = Circulo(radio)
            probarFigura(c1)
        elif opcion == "3":
            print("fin")
            break
        else:
            print("Ingrese una opcion valida")

if __name__=="__main__":
    main()