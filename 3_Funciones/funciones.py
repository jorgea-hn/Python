#FUNCIONES

def saludar():
    global nombre
    nombre = "Jorge Henriquez"
    edad = 25
    return "Hola desde la funcion saludar",nombre,edad
    

# print(saludar())
# print("Hola desde fuera de la funcion", nombre)

saludo,nombre,edad = saludar()
print(saludo)
print(nombre,edad)

#----------Parametros y argumentos
def saludar1(nombre):
    return f"Hola {nombre}"

print(saludar1("jorge"))

def restar(a=None, b=None):
    if a ==None or b==None:
        print("Error: debes enviar dos numeros a la funcion")
        return
    return a-b

resta = restar()
print("La resta es", resta)


#-----Argumentos indeterminados
def sumar(*args, **kwargs): 
    suma = 0
    for n in args:
        suma += n
    return suma, kwargs

print(sumar(1,2,3,4,5,6,nmbre = "Jorge", edad=25))
# *args = guarda los valores como una tupla
# **kwargs = guarda los valores como un diccionario

#----Funcion Recursiva
def factorial(n):
    print("Valor inicial",n)
    if n > 1:
        n = n * factorial(n-1)
    print("Valor final",n)
    return n

print(factorial(3))


#-----Lambda
sumar = lambda a,b : a+b

print(sumar(10,20))

doblar = lambda n : n*2
print(doblar(5))

par = lambda n : n%2==0
print(par(4))

inpar = lambda n: n%2 !=0
print(inpar(5))

revertir = lambda cadena : cadena[::-1]
print(revertir('hola'))

#-----Funciones integradas
print(eval("2+5")) #evalua una cadena de caracteres y decir si se puede operar o no
print(bin(10))
print(int(0b1010))
print(hex(10))
# help()

#----Metodos de las cadenas de caracteres
print("Hola mundo".upper()) #Colocar todo en mayuscula
print("Hola Mundo".lower()) #colocar todo en minuscula
print("hola mundo".capitalize()) #colocar la primera letra de la primera palabra en mayuscula
print("hola mundo".title()) #coloca la primera letra de cada palabra en mayuscula
print("Hola mundo".count("o")) #cuenta cuantas letras iguales hay
print("Python".replace("P","S")) #reemplaza la letra
print("P y t h o n".replace(" ",""))# reemplaza lo que necesitas 
print("   Hola mundo    ".strip())
# elimina los digitos de la derecha e izquierda de la palabra
print("------Hola-mundo---------".strip("-")) # elimina los digitos de la derecha e izquierda de la palabra
print("Hola mundo".split()) #devuelve una lista 
print("Hola,mundo,de,python".split(","))
#devuelve una lista separandolos por coma
print("hola".islower())
#pregunta si la palabra esta en minuscula
#debe estar toda en minuscula y devuelve un booleano
print("HOLA".isupper())
