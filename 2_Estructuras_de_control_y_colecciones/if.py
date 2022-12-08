#ESTRUCTURAS CONTROL DE FLUJO

# Sentencia If y Else
if True:
    print("Se cumple la condicion")

if False:
    print("Se cumple la condicion") #Esta condicion no se cumple

if False:
    print("Se cumple la condicion")
else:
    print("No se cumplio la condicion if")


print("Detector de numero par o inpar")
n = int(input("Ingrese su numero: "))

if(n%2==0):
    print(f"El numero {n} es par")
else:
    print(f"El numero {n} es inpar")

#--------------Condiciones anidadas--

print("Detector de numero par o inpar mejorado")
n = int(input("Ingrese su numero: "))

if n!=0:
    if n > 0:
        if n % 2 == 0:
            print(f"El numero {n} es par positivo")
        else:
            print(f"El numero {n} es inpar positivo")
    else:
        if n % 2 == 0:
            print(f"El numero {n} es par negativo")
        else:
            print(f"El numero {n} es inpar negativo")
else:
    print(f"El numero {n} es neutro")


#------------Multiples condiciones------------
letra = input("Ingrese su letra: ")

if letra =="a" or letra=="A":
    print(letra, "Es vocal")
elif letra =="e" or letra=="E":
    print(letra, "Es vocal")
elif letra =="i" or letra=="I":
    print(letra, "Es vocal")
elif letra =="o" or letra=="O":
    print(letra, "Es vocal")
elif letra =="u" or letra=="U":
    print(letra, "Es vocal")
else:
    print(letra,"No es vocal")




