class OperadorExcepcion(Exception):
    def __init__(self,mensaje):
        super().__init__(mensaje)

def div(a,b):
    if b==0:
        raise OperadorExcepcion("Error: No se puede dividir entre 0")
    else: 
        return a/b

print(div(4,0))