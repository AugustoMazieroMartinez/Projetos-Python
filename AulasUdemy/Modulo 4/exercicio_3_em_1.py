# Exercicions
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90}
]
for produto in produtos:
    produto['preco'] *= 1.1
novos_produtos = produtos.copy()
print(novos_produtos)

# Ordene os produtos por nome decrescente (do maios para menor)
# Gere produtos_ordenados por deep copy (cópia profunda)
for i in range(len(produtos)):
    for j in range(i+1, len(produtos)):
        if produtos[i]['nome'] < produtos[j]['nome']:
            produtos[i], produtos[j] = produtos[j], produtos[i]
produtos_ordenados = produtos.copy()
print(produtos_ordenados)
# Ordene os produtos por preço crescente (do menor para o maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
for i in range(len(produtos)):
    for j in range(i+1, len(produtos)):
        if produtos[i]['preco'] > produtos[j]['preco']:
            produtos[i], produtos[j] = produtos[j], produtos[i]
produtos_ordenados_por_preco = produtos.copy()
print(produtos_ordenados_por_preco)