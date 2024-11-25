lista = []

for x in range(10):
    for y in range(10):
        lista.append((x,y))
print(lista)
lista = [
        (x, y) 
        for y in range(10) 
        for x in range(10)
]
print(lista)