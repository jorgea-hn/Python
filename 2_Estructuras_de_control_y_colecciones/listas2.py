# datos = ["jorge","Henriquez",25]

# a = datos.append(186) # inserta un dato en la ultima posicion
# print(a)
# b = datos.extend(datos)  # agrega un elemento al final
# print(b)
# c = datos.insert(0,100) # inserta un dato en la posicion que queremos
# print(c)
# d= datos.remove(100)  # remueve el dato
# print(d)
# e = datos.pop() #elimina el ultimo elemento
# print(e)
# f = datos.clear() # elimina toda la lista
# print(f)
# g = datos.index(25) # te da la posicion de un valor
# print(g)
# h = datos.count(100) #cuenta si se repite un valor
# print(h)

# frutas = ["Naranja", "uva","aguacate","Limon"]
# i = frutas.sort()  #ordena la lista
# print(i)

# datos = [1,2,3,4,5]
# j = datos.reverse()  #Invierte la lista
# print(j)


#-----------------pila------
pila = [1,2,3,4,5]
pila.append(6)
pila.append(7)
pila.pop()

#-----------------cola------
from collections import deque
cola = deque(["jorge","juan","camilo"])
cola.append("purrin")
print(cola)
cola.popleft()
print(cola)