
# Primera variable
x = 10

# Variable none
n = None

# Multiples variables
a,b,c =10,20,30

# Dato flotante
dato = 2.5

# Dato String
frase = "Hola mundo"
frase1 = 'Hola mundo de programacion'

# Los nombres de las variables deberian ser en minusculas
nombre = "Jorge Henriquez"

#Las variables correctas
_texto = "Hola"
n1 = 1


#Las variables incorrectas
# hola mundo = "Hola"
# 1n = 10
# -hola = "error"  No se pueden utilizar barra al medio
# dolar$ = 3.52    No se pueden utilizar signos
# None = "Vacio"   No se pueden utilizar variables reservadas


#-----------Operaciones----------------
valor1 = 10
valor2 = 40

total = valor1 + valor2
print(total)


valor3 = 12.6
valor4 = 12.67

total1 = valor3*valor4

#redondear
print(round(total1,2))

# Tipos de datos
print(type(24))
print(type(24.4))
print(type("Hola"))
print(type(2j))
print(type([1,2,3]))


#------Cadena de caracteres---------
print('Hola mundo')

#Caracteres especiales
print('Hola \' mundo')
print('Hola "\'" mundo')
print("Hola \nmundo")    #Salto de linea
print('Hola \tmundo')    #Tabulador

print(r'C:some\name')    #Ruta de directorio
print("""
    Buenas tardes
    Mi nombre es jorge
    Aprendiendo
    Muchas gracias
""")


#-------Operacion con cadenas de caracteres----------
texto ="Hola"

print(texto*3)
print(texto+texto)
print(3*"un"+"ium")
print("Hola" "mundo")

p = "Py"
print(p+"thon")

palabra = "Python"
print(palabra)


#Trozos

print(palabra[0])   #acceder al primer indice
print(palabra[-1])  #accder al ultimo indice

print(palabra[0:2]) 
print(palabra[:2])

print(palabra[2:])

#Las cadenas son inmutables
print("S"+palabra[1:])

#Funcion len
print(len(palabra))


