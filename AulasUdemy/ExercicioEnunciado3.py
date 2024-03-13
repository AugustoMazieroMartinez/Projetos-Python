nome = input('Digite seu nome: ')
if len(nome) <= 4:
    print('Seu Nome é Curto')
elif len(nome) >= 5 and len(nome) <= 6:
    print('Seu Nome é Normal')
else:
    print('Seu Nome é Longo')