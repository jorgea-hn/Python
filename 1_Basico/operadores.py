#Operadores Relacionales
a=10
b=5

print(a==b)
print(a==a)
print(a!=b)
print(a>b)
print(a<b)
print(a<b)
print(a>=b)
print(a<=b)
print(4==4)
print("Hola"=="Hola")
print("Hola"=="hola")


#Operadores logicos
a=10
b=5
#AND devuelve valor booleano de la comparacion de dos valores que ambos deben ser verdaderos
print((a==b) and (a!=b))

#OR devuelve valor booleano de la comparacion de dos valores que uno de los valores es verdadero
print((a==b) or (a!=b))

#NOT Deniega
print((a==b) or not (a!=b))

#Expresion anidada
print(a*b -2 **b >= 20 and not (a%b)!=0)

print(a*b -2 **b >= 20 or not (a%b)!=0)


#Operadores en asignacion

a = 10
a = a + 5  # Esta linea se simplifica con la linea siguiente
a += 5
print(a)

a-=5
print(a)

a*=5
print(a)

a/=5
print(a)

a//=5
print(a)

a**=2
print(a)

a%=5
print(a)


# operador de identidad
texto1 = "hola"
texto2 = "hola"

print(texto1 is texto2)

texto2 = "Hola"
print(texto1 is texto2)
print(texto1 is not texto2)

#Operadores de pertenencia
texto = "Hola mundo"

print("h" in texto)
print("H" in texto)

nombres = ["alex", "roel",25]
print(25 in nombres)

print("Juan" not in nombres)

#Operadores booleanas
print(False*5)
print(True*5)