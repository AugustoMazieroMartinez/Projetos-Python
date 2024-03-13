numero_str = input("Digite um numero para ser dobrado: ")
# if numero_str.isdigit():
#     
# else:
#     print("Por favor digite um número!!!")

try:
    print("STR: ", numero_str)
    numero_int = int(numero_str)
    print('INT: ', numero_int)
    print(f'O dobro de {numero_str} é igual a {numero_int * 2}')
except:
    print('Isso não é um número')