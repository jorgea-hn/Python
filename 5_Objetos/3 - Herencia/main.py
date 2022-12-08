from persona import Cliente,Empleado

cliente1 = Cliente("Alex",25)
cliente2 = Cliente("Jorge",25)
cliente1.detalle_persona()
print(cliente2)

empleado1 = Empleado("Jorgito",25,2000)
empleado2 = Empleado("juan",18,1000)

empleado1.detalle_persona()
empleado1.detalle_empleado()

print(empleado2)