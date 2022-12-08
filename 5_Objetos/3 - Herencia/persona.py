class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def detalle_persona(self):
        print(f"Nombre: {self.nombre} \nEdad: {self.edad}")


    def __str__(self):
        return f"Nombre: {self.nombre} \nEdad: {self.edad}"
    

class Cliente(Persona):
    pass

class Empleado(Persona):
    def __init__(self, nombre,edad,sueldo):
        # super().__init__(nombre,edad)
        Persona.__init__(self,nombre,edad)
        self.sueldo = sueldo
    
    def detalle_empleado(self):
        # super().detalle_persona()
        Persona.detalle_persona(self)
        print("Sueldo", self.sueldo)

    def __str__(self):
        #super().__str__() + f"\nSueldo {self.sueldo}"
        return Persona.__str__(self) + f"\nSueldo {self.sueldo}"
        
    