def div(a,b):
    if b==0:
        raise ZeroDivisionError("Error: No se puede dividir entre 0")
    else: 
        return a/b

print(div(4,0))