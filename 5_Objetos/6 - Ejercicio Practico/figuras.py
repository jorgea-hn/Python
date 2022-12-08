import math
class Figura():
    def __init__(self,nombre):
        self.nombre = nombre

    def area(self):
        pass

    def perimetro(self):
        pass

    def __str__(self):
        return f"\nNombre: {self.nombre}"

class Rectangulo(Figura):
    
    # def __init__(self,base,altura):
    #     super().__init__(base,altura)
    def __init__(self, base,altura):
        self.nombre = __class__.__name__
        self.base=base
        self.altura=altura

    def area(self):
        return self.base* self.altura

    def perimetro(self):
        return 2*(self.base+self.altura)

    def __str__(self):
        return super().__str__() + f"\nBase: {self.base} \nAltura: {self.altura} "

class Circulo(Figura):
    def __init__(self, radio):
        self.nombre = __class__.__name__
        self.radio=radio
    
    def area(self):
        return round(math.pi*(self.radio**2),2)

    def perimetro(self):
        return round(2*math.pi*self.radio,2)

    def __str__(self):
        return super().__str__() + f"\nRadio: {self.radio}"

def probarFigura(figura):
    print(figura)
    print("Area: ",figura.area())
    print("Perimetro: ", figura.perimetro())
    