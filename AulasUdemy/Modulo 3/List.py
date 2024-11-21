import pprint as pp
# print(list(range(10)))
# lista = []
# for numero in range(10):
#     lista.append(numero)
# print(lista)

# lista = [numero for numero in range(10)]
# print(lista)
# def p(v):
#     pp.pprint(v, sort_dicts=True)
# produtos = [
#     {'nome': 'p1', 'preco': 20},
#     {'nome': 'p2', 'preco': 30},
#     {'nome': 'p3', 'preco': 40}
# ]

# novos_produtos = [
#     {**produto, 'preco': produto['preco'] * 1.05}
#     if produto['preco'] > 20 else {**produto}
#     for produto in produtos
# ]

# print(novos_produtos)
# print(*novos_produtos, sep='\n=========================== \n')


lista = [n for n in range(100) if n]
print(lista)