#Entrada de datos y casteo

print("Suma de dos numeros enteros")
dato1 = int(input("Ingrese el primer valor: "))
dato2 = int(input("Ingrese el primer valor: "))

suma = dato1 + dato2
print(f'Su suma es igual a {suma}')



"""Cociente y residuo"""
dato1 = float(input("Ingrese el primer valor: "))
dato2 = float(input("Ingrese el primer valor: "))

cociente = dato1 / dato2
residuo = dato1 % dato2

print(f'El cociente es {cociente} y el residuo {residuo}')

#Calcular precio de venta
print("Vamos a calcular el precio de venta")
valor = float(input("Ingrese el valor del producto: "))

igv = valor* 0.18
pv = valor + igv

print(f"El IGV es {igv} y el precio de venta es {pv}")