# groupby - agrupando valores (itertools)

from itertools import groupby as group

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rose', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'B'},
    {'nome': 'Carlos', 'nota': 'A'},
    {'nome': 'Julia', 'nota': 'B'},
    {'nome': 'Lara', 'nota': 'C'},
    {'nome': 'Ana', 'nota': 'A'},
    {'nome': 'Luiza', 'nota': 'B'},
]
grupos = sorted(alunos, key=lambda a: a['nota'])
grupos = group(grupos, lambda a: a['nota'])
for chave, grupo in grupos:
    print(chave)
    print(list(grupo))