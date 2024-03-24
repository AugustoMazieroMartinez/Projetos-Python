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
            try:
                apagar = input('Índice do valor a ser apagado: ')
                index = int(apagar)
                del lista_compras[index]
                os.system('cls')
                print('O valor for removido!')
                continue
            except IndexError:
                print('O índice não existe na lista.')
                continue
            except ValueError:
                print('Por favor digite um número int.')
                continue
            except Exception:
                print('Erro desconhecido.')
        else:
            os.system('cls')
            print('Não há valores na lista para serem apagados!\n')
            continue
    if entrada == 'l':
        if len(lista_compras) != 0:
            os.system('cls')
            for indice, valor in enumerate(lista_compras):
                print(indice, valor)
            continue
        else:
            os.system('cls')
            print('Nada para listar\n')
            continue