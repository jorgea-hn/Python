# 1 = piedra
# 2 = tijera
# 3 = papel

import random

def jugar():
    numero = random.randint(1,4)
    numero_jugador = None
    roles = {1:"Piedra",2:"Tijera",3:"Papel"}
    print("""

    """)
    jugador = input("Ingrese su nombre: ")
    jugadorU = jugador.upper()
    while numero!=numero_jugador:
        menuJuego = """
        ------------------
        ------------------
        Menu del Juego
        1 - Piedra
        2 - Tijera
        3 - Papel
        INGRESE UNA OPCION: """

        numero_jugador = int(input(menuJuego))

        print("""
    
        """)
        resultado = f"COMPUTADORA: {roles[numero]}  \n{jugadorU}: {roles[numero_jugador]}" 

        if numero==1:
            if numero_jugador==1:
                print(resultado)
                print("Empate")
            elif numero_jugador==2:
                print(resultado)
                print("Perdiste")
            elif numero_jugador==3:
                print(resultado)
                print("Ganaste")
        if numero==2:
            if numero_jugador==1:
                print(resultado)
                print("Ganaste")
            elif numero_jugador==2:
                print(resultado)
                print("Empataste")
            elif numero_jugador==3:
                print(resultado)
                print("Perdiste")
        if numero==3:
            if numero_jugador==1:
                print(resultado)
                print("Perdiste")
            elif numero_jugador==2:
                print(resultado)
                print("Ganaste")
            elif numero_jugador==3:
                print(resultado)
                print("Empataste")


def main():
    while True:
        menu = """
        PIEDRA PAPEL O TIJERA
        1 - Jugar
        2 - Salir
        INGRESE UNA OPCION: """

        opcion = input(menu)

        if opcion=="1":
            jugar()
        elif opcion=="2":
            print("CERRANDO JUEGO")
            break
        else:
            print("Opcion incorrecta vuelve a intentar")
        

if __name__ == "__main__":
    main()