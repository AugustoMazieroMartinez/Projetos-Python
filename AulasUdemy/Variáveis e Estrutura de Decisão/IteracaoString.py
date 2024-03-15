frase = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'\
    ' Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s.'
index = 0
apareceu_mais_geral = 0
letra_mais_frequente = ''

while index < len(frase):
    letra_atual = frase[index]
    
    if frase[index] == ' ':
        index += 1
        continue
    
    apareceu_mais_atual = frase.count(letra_atual)
    
    if apareceu_mais_geral  < apareceu_mais_atual:
        apareceu_mais_geral = apareceu_mais_atual
        letra_mais_frequente = letra_atual
    
    index += 1
    
print(f'A letra mais frequente é {letra_mais_frequente} 
      e a sua quantia de repetições é {apareceu_mais_geral}')