#EJERCICIO DE RESTAURANTE
#----------ejercicio de estructura de control---

valor = float(input("Ingrese su valor de consumo: "))


if(valor<=100):
    des = "10%"
    descuento = valor * 0.1
else:
    des = "20%"
    descuento = valor * 0.2

impuesto = (valor-descuento)*0.19
montoDesc = valor-descuento
total = valor-descuento+impuesto

print("="*20)
print("----Factura----")
print("Descuento de ", des)
print("="*20)
print("Descuento: ", descuento)
print("Monto con descuento: ", montoDesc)
print("Inpuesto: ",impuesto )
print("Importe a pagar: ", total )
print("="*20)


