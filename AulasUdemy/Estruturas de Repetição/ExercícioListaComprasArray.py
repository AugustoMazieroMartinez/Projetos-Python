import os
lista_compras = []
while True:
    print(f'Selecione uma opção\n')
    entrada = input('[i]nserir [a]pagar [l]istar: ')
    if entrada == 'i':
        inserir = input('Valor: ')
        lista_compras.append(inserir)
        os.system('cls')
        print('Valor Inserido!')
        continue
    if entrada == 'a':
        if len(lista_compras) != 0:
            apagar = input('Índice do valor a ser apagado: ')
            lista_compras.remove(int(apagar))
            os.system('cls')
            print('O valor for removido!')
            continue
        else:
            print('Não há valores na lista para serem apagados!\n')
            continue
    if entrada == 'l':
        if len(lista_compras) != 0:
            for indice, valor in enumerate(lista_compras):
                print(indice, valor)
            continue
        else:
            print('Nada para listar\n')
            continue