a = set()
type(a)

a={"a","b","c"} # no se pueden elementos repetidos
print(a)

a={"a","b","c","a"}
print(a)

a = set("abracadabra")
print(a)

b= set("alacazam")

print(a-b) #devuelve las letras que estan en a y no en b
print(a|b) #devuelve las letras que estan en a y b y no se repiten
print(a&b) #devuelve las letras que estan en a y en b
print(a^b) #devuelve las letras que estan en a y en b pero que no esta en ambos


a = {"a","b","c"}
a.add("d")  #agrega un valor
print(a)

a.discard("b") #elimina un valor
print(a)

a.clear()  #elimina todo del cojunto
print(a)


#del---------------------
a = ["a","b","c","d"]
del a[0]    #elimina algo de la lista o toda la lista


d={"uno":1,"dos":2}
del d["dos"]
print(d)
