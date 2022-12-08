#EJERCICIO DE RESTAURANTE
#----------ejercicio de estructura de control---

valor = float(input("Ingrese su valor de consumo: "))


if(valor<=100):
    des = "10%"
    descuento = valor * 0.1
elif(valor>100 and valor<=200):
    des = "20%"
    descuento = valor * 0.2
elif valor>200:
    des= "30%"
    descuento = valor * 0.3

impuesto = (valor-descuento)*0.19
montoDesc = valor-descuento
total = valor-descuento+impuesto

print("="*20)
print("----Factura----")
print("Descuento de ", des)
print("="*20)
print("Valor:", valor)
print("Descuento: ", descuento)
print("Monto con descuento: ", montoDesc)
print("Inpuesto: ",impuesto )
print("Importe a pagar: ", total )
print("="*20)