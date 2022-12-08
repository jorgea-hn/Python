#TUPLAS
t = ("Jorge",25,1.86)
print(t[0])
print(t[:2])

#Las tuplas no se pueden modificar 
print(len(t))
print(t.index(25))


#DICCIONARIOS
numeros = {}
numeros = {"uno":1,"dos":2,"tres":3,"cuatro":4}

print(numeros)
print(numeros["uno"])
numeros["cinco"]=5
print(numeros)
print(numeros.get("cuatro","No se encontro"))

print(numeros.keys()) # devuelve todas las claves
print(numeros.values()) # devuelve todos los valores

print(numeros.items())

numeros.pop("cinco","No se encontro") #elimina un elemento y si no se encuentra devuelve el mensaje
print(numeros)

for numero in numeros:
    print(numero)

for numero in numeros.values():
    print(numero)

for clave, valor in numeros.items():
    print(clave,valor)


numeros.clear()