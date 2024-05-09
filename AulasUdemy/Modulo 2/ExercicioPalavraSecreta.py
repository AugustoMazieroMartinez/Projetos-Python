import	os

PALAVRA_SECRETA = 'amogus'
palavra_formatada = '*' * len(PALAVRA_SECRETA)
tentativas = 0
while palavra_formatada != PALAVRA_SECRETA:
    print(f'Palavra Formatada: {palavra_formatada}')
    letra_digitada = input("Digite Apenas Uma Letra: ")
    
    if len(letra_digitada) > 1:
        print('Digite Apenas Uma Letra!!! ')
        continue

    for i, char in enumerate(PALAVRA_SECRETA):
        if letra_digitada == char:
            palavra_formatada = palavra_formatada[:i] + letra_digitada + palavra_formatada[i + 1:]

    tentativas += 1
os.system('cls')
print(f'Você Acertou!!! \nA Palavra era: {PALAVRA_SECRETA} \nTentativas: {tentativas}')