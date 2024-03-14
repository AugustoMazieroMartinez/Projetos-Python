continuar = True
while continuar:
    pNumero = input('Digite o Primeiro Número: ')
    sNumero = input('Digite o Segundo Número: ')
    num_pNumero = 0
    num_sNumero = 0
    resultado = 0.0
    nValidos = None
    operadores = '+-*/'
    print('Escolha o Tipo de Operação')
    escolha = input('1 - Soma [+] \n2 - Subtração [-] \n3 - Multiplicação [*] \n4 - Divisão  [/] \n')
    try:
        num_pNumero = float(pNumero)
        num_sNumero = float(sNumero)
        nValidos = True
    except:
        nValidos = None
    if nValidos is None:
        print('Um ou ambos os Números Digitados são Inválidos')
        continue
    if escolha not in operadores:
        print('Digite um Operador Válido')
        continue
    if len(escolha) > 1:
        print('Escolha apenas um operador')
        continue
    if escolha == '+':
        print(num_pNumero + num_sNumero)
    elif escolha == '-':
        print(num_pNumero - num_sNumero)
    elif escolha == '*':
        print(num_pNumero * num_sNumero)
    else:
        print(num_pNumero / num_sNumero)    
    
    sair = input('Deseja sair? [s]im: ').lower().startswith('s')
    if sair is True:
        break
print('Fim do Código')