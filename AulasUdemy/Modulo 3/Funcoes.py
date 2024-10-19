# def repete(str):
#     for i in range(10):
#         print(str)
# repete(input('Digite algo para ser repetido 10 vezes: '))


#Exercícios:
def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    print(total) 
def parImpar(x):
    if x % 2 == 0:
        print('Par')
    else:
        print("Impar")
        
multiplica(1,2,3,4,5)
parImpar(5)