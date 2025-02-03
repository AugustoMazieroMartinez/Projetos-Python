# Funções decoradoras e decoradores
# Decorar = adicionar / romover / restringir / alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# Usar as funções decoradoras em outras funções
# Decoradores são "Syntax Sugar" (açúcar sintático)	

def criar_funcao(funcao): # Função Decoradora
    def interna(*args, **kwargs):
        for arg in args:
            e_string(arg)
        resultado = funcao()
        return resultado
    return interna

@criar_funcao
def inverte_string(string):
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise ValueError('Somente string é permitida')


invertida = inverte_string('123')
print(invertida)