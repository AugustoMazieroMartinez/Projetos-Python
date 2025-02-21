import json as js

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
dados = {
    'nome': 'Jeremias',
    'idade': 22
}
p1 = Pessoa(**dados)
js_data = js.dumps(p1.__dict__)
print(js_data)
        
with open("dados.json", "w") as arquivo:
    arquivo.write(js_data)