valores = []
media = 0
valores.append(float(input('Digite um valor a ser Adicionado à média: ')))
while True:
    resp = input('Deseja adicionar mais um? (s/n) ')
    
    if resp == 's':
        valores.append(float(input('Digite um valor a ser Adicionado à média: '))) 

    else:
        media = sum(valores)/len(valores)
        break
print(media)