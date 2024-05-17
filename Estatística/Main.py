from Node import Node
from Lista_sort import Lista_Sort as Lista
from random import seed, random

seed(100)
lista = Lista()
for i in range(100):
    lista.append(random())
    
lista.bubble_sort()
lista.display()