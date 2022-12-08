c = 0
while c < 10:
    c += 1
    print(c)
    if c ==5:
        print("Termina el bucle")
        break
else:
    print("Fin del while")


c = 0
while c < 10:
    c += 1
    print(c)
    if c ==5:
        print("Termina el bucle")
        continue
    print("Despues del continue")
else:
    print("Fin del while")