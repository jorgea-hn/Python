import random
def ahorcado():
    animales = ["perro","gato","condor","conejo","leon","tigre","dinosaurio",
    "caballo","burro","mapache","ornitorrinco","cerdo", "jaguar","gorila",
    "pez","hamster", "leopardo", "raton"]
    # deportes = ["futbol","backetball","volleyball","tennis","natacion","ciclismo"]
    a = random.randint(1,len(animales))
    # d = random.randint(1,len(deportes))
    
    while True:
        morgue = """
             -----------------------------
             ---                       ---
              |                        ---
              |                        ---
                                       ---
                                       ---
                                       ---
                                       ---
                                       ---
                                       ---
                                       ---
                                       ---
                                       ---
                                       ---
                                       ---
                                       ---
        """
        cabeza = """
             -----------------------------
             ---                       ---
              |                        ---
             ***                       ---
           **   **                     ---
             ***                       ---
                                       ---
                                       ---
                                       ---
                                       ---
                                       ---
                                       ---
                                       ---
                                       ---
                                       ---
                                       ---
                                       ---
        """

        cuerpo = """
             -----------------------------
             ---                       ---
              |                        ---
             ***                       ---
           **   **                     ---
             ***                       ---
              *                        ---
              *                        ---
              *                        ---
              *                        ---
                                       ---
                                       ---
                                       ---
                                       ---
                                       ---
                                       ---
                                       ---
        """

        piernaI = """
             -----------------------------
             ---                       ---
              |                        ---
             ***                       ---
           **   **                     ---
             ***                       ---
              *                        ---
              *                        ---
              *                        ---
             ***                       ---
                *                      ---
                 *                     ---
                  *                    ---
                   *                   ---
                    *                  ---
                                       ---
                                       ---
        """

        piernaD = """
             -----------------------------
             ---                       ---
              |                        ---
             ***                       ---
           **   **                     ---
             ***                       ---
              *                        ---
              *                        ---
              *                        ---
             ***                       ---
            *   *                      ---
           *     *                     ---
          *       *                    ---
         *         *                   ---
        *           *                  ---
                                       ---
                                       ---
        """

        brazoI = """
             -----------------------------
             ---                       ---
              |                        ---
             ***                       ---
           **   **                     ---
             ***                       ---
             ****                      ---
              *  *                     ---
              *   *                    ---
             ***   *                   ---
            *   *                      ---
           *     *                     ---
          *       *                    ---
         *         *                   ---
        *           *                  ---
                                       ---
                                       ---
        """

        brazoD = """
             -----------------------------
             ---                       ---
              |                        ---
             ***                       ---
           **   **                     ---
             ***                       ---
            *****                      ---
           *  *  *                     ---
          *   *   *                    ---
         *   ***   *                   ---
            *   *                      ---
           *     *                     ---
          *       *                    ---
         *         *                   ---
        *           *                  ---
                                       ---
                                       ---
        """


        menu = """
        OPCIONES
        1 - Jugar
        2 - Salir
        Ingrese una opcion: """
        opcion = input(menu)

        if opcion == "1":
            a = random.randint(1,len(animales))
            animal = animales[a]
            animalM = animal
            for x in animal:
                  animalM= animalM.replace(x,"_")
            intentos = 8
            correcta = 0 

            while True:
                letra = input("Ingrese una letra: ")

                if letra in animal:
                    for x in range (0,len(animal)):
                        if letra == animal[x]:
                            # print("La letra se encuentra: ",x)
                            animalM = list(animalM)
                            animalM[x] = letra
                            correcta +=1
                    print("-------------------------------")
                    print("El animal es :", animalM)
                    if "_" not in animalM:
                        print("Ganador Usted es el mejor!!!")
                        break
                else:
                    print("La letra no se encuentra")
                    print("-------------------------------")
                    print("El animal es :", animalM)
                    intentos = intentos - 1
                
                if intentos == 7:
                    print(morgue)
                if intentos == 6:
                    print(cabeza)
                elif intentos == 5:
                    print(cuerpo)
                elif intentos == 4:
                    print(piernaI)
                elif intentos == 3:
                    print(piernaD)
                elif intentos == 2:
                    print(brazoI)
                elif intentos == 1:
                    print(brazoD)
                elif intentos == 0:
                    print("Game Over")
                    break

        if opcion==2:
            print("GAME OVER")
            break
                    





def main():
    ahorcado()
    # while True:
    #     menu = """
    #     AHORCADO
    #     1 - Nivel Facil
    #     2 - Nivel Medio
    #     3 - Salir
    #     INGRESE UNA OPCION: """
    #     opcion = input(menu)

    #     if opcion=="1":
    #         ahorcado()
    #     elif opcion=="2":
    #         ahorcado()
    #     elif opcion=="3":
    #         print("CERRANDO JUEGO")
    #         break
    #     else:
    #         print("Opcion incorrecta vuelve a intentar")

if __name__ == "__main__":
    main()