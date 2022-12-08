c = 0 
suma = 0 
while c < 3:
    try:
        n = int(input(f"Ingrese un numero {c+1}: "))
        suma+=n
        c+=1
    except:
        print("Ingrese solo numeros enteros: ")
    else:
        print("Todo ha funcionado correctamente")
    finally:
        print("Fin de la ejecucion")

print("La suma es: ", suma)
