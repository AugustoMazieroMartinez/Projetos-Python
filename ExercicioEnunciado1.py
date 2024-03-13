numero = input("Digite um número Inteiro: ")

if numero.isdigit:
    if int(numero) % 2 == 0:
        print('O Número digitado é par')
    else:
        print('O Número digitado é impar')