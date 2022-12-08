#-----Primalidad
"""def primo(n):
    if n==1:
        print("Numero no Primo")
    else:
        c = 0
        for i in range (1,10):
            if n%i==0:
                c+=1
        if c <= 2:
            print("Numero Primo")
        else:
            print("Numero no primo")

n = int(input("Ingrese un numero: "))
primo(n)"""


def primo(n):
    if n==1:
        return False
    else:
        c = 0
        for i in range (1,10):
            if n%i==0:
                c+=1
        if c <= 2:
            return True
        else:
            return False

#Funcion principal
def main():
    n = int(input("Ingrese una numero: "))
    es_primo = primo(n)

    if es_primo:
        print("Es primo")
    else:
        print("No es primo")


#Punto de la entrada de la aplicacion
if __name__ == "__main__":
    main()