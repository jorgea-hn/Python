
directorio = []

def usuarios():
    nombre = input("Ingrese nombre del usuario: ")
    apellido = input("Ingrese apellido del usuario: ")
    numero = input("Ingrese numero del usuario: ")
    usuario = [nombre,apellido,numero]
    return usuario

def agregar():
    if len(directorio) == 0:
        global u 
        u = usuarios()
        directorio.append(u)
        print(directorio)
    elif len(directorio) > 0:
        x = buscar()
        if x==True:
            print("Usuario Existente")
        else:
            directorio.append(u)

def buscar():
    u = usuarios()
    for usuarios in directorio:
        if u == usuarios:
            return True
        else:
            return False

def eliminar():
    pass



def main():
    while True:
        menu="""
        MENU DE DIRECTORIO
        1 - Agregar Contacto
        2 - Buscar Contacto
        3 - Eliminar Contacto
        4 - Actualizar Contacto
        INGRESE UNA OPCION: """

        opcion = input(menu)
        print(opcion)

        if opcion=="1":
            agregar()
            

if __name__ == "__main__":
    main()