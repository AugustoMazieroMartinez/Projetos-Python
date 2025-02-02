import sys
lista = [x for x in range(1000000000)]
generator = (x for x in range(10000))
for x in lista:
    if x == 1000000000:
        print(x)
print(sys.getsizeof(lista))