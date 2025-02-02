# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

def executa(funcao, *args):
    def interna():
        return funcao(*args)
    return interna

soma_com_cinco = executa(soma, 5)
multiplica_por_dez = executa(multiplica, 10)