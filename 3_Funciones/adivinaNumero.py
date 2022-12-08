import random

def jugar(vidas):
     numero = random.randint(1,100)
     numero_jugador = None

     while numero != numero_jugador:
        numero_jugador = int(input("Ingrese un numero entre 1 y 100: "))

        if numero < numero_jugador:
            print("Elige un numero mas pequeño")
            vidas -=1
        elif numero > numero_jugador:
            print("Elige un numero mas grande")
            vidas -=1

        if vidas==0:
            print("GAME OVER!")
            break

        print(f"Te quedan {vidas} vidas")

        if numero_jugador == numero:
            print("FELICIDADES GANASTE!!!!")

def main():
    while True:
        menu = """
        ADIVINA EL NUMERO ALEATORIO
        1 - Nivel Facil
        2 - Nivel Intermedio
        3 - Nivel Dificil
        4 - Salir
        INGRESE UNA OPCION: 
        """

        opcion = input(menu)

        if opcion=="1":
            jugar(10)
        elif opcion=="2":
            jugar(7)
        elif opcion=="3":
            jugar(5)
        elif opcion=="4":
            print("CERRANDO JUEGO")
            break
        else:
            print("Opcion incorrecta vuelve a intentar")
        

if __name__ == "__main__":
    main()