pNumero = input('Digite o Primeiro Número: ')
sNumero = input('Digite o Segundo Número: ')
resultado = 0.0

print('Escolha o Tipo de Operação')
escolha = input('1 - Soma \n2 - Subtração \n3 - Multiplicação\n4 - Divisão \n')
if pNumero.isdigit and sNumero.isdigit:
    soma = float(pNumero) + float(sNumero)
    sub = float(pNumero) - float(sNumero)
    mult = float(pNumero) * float(sNumero)
    div = float(pNumero) / float(sNumero)
    if escolha.isdigit == True:
        if int(escolha) == 1:
            print(soma)
        elif int(escolha) == 2:
            print(sub)
        elif int(escolha) == 3:
            print(mult)
        elif int(escolha) == 4:
            print(div)
        else:
            print('O valor que você digitou na escolha não é válido')
    else:
        if escolha == 'Soma': 
            print(soma)
        elif escolha == 'Subtração':
            print(sub)
        elif escolha == 'Multiplicação':
            print(mult)
        elif escolha == 'Divisão':
            print(div)
        else: 
            print('O valor que você digitou na escolha não é válido')
else:
    print('Digite Apenas Números!!!')