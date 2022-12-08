class A:
    def __init__(self):
        print("Soy clase A")
    def a(self):
        print("Soy metodo de A")

class B:
    def __init__(self):
        print("Soy clase B")
    def b(self):
        print("Soy metodo de B")

class C(B,A):
    def c(self):
        print("Soy metodo de C")

c1 = C()
print(c1)

class C(A,B):
    def c(self):
        print("Soy metodo de C")
c2 = C()
print(c2)

print(c1.a())
print(c1.b())
print(c1.c())