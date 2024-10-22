# def repete(str):
#     for i in range(10):
#         print(str)
# repete(input('Digite algo para ser repetido 10 vezes: '))


# #Exercícios:
# def multiplica(*args):
#     total = 1
#     for numero in args:
#         total *= numero
#     print(total) 
# def parImpar(x):
#     if x % 2 == 0:
#         print('Par')
#     else:
#         print("Impar")
        
# multiplica(1,2,3,4,5)
# parImpar(5)

# def dup(x):
#     return x * 2
# def trip(x):
#     return x * 3
# def quad(x):
#     return x * 4
def mult(x):
    def multiplica(y):
        return y * x
    return multiplica
duplicar = mult(2)
triplicar = mult(3)
quad = mult(4)
x = 5
print(duplicar(x), triplicar(x), quad(x))
