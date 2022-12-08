import sys
#print(sys.argv)

if len(sys.argv)==3:
    texto = sys.argv[1]
    cantidad = int(sys.argv[2])

    c = 0
    while c<cantidad:
        print(texto)
        c+=1
else:
    print("Error, Ingrese los argunmentos correctamente")
    print('Ejemplo: entra_script "texto" 5')