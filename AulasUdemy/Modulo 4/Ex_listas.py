# Exercício - Unir Listas
# Crie uma função zipper
# O trabalho da função é unir duas listas na ordem
# Use todos os balores da menor lista
# Ex:
# ['Salvador'. 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado:
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def zipper1(lista1, lista2):
    min_length = min(len(lista1), len(lista2))
    return [(lista1[i], lista2[i]) for i in range(min_length)]

def zipper2(lista1, lista2):
    return list(zip(lista1, lista2))
    
lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']

print(zipper1(lista1, lista2))
print(zipper2(lista1, lista2))