mensagem = input() # 'papo papa'
palavras = mensagem.split() # ['papo', 'papa']
palavras_decodificadas = []
for palavra in palavras: # 'papo'
    # lógica de decodificação
    palavra_decodificada = palavra[1::2]
    palavras_decodificadas.append(palavra_decodificada)
print(' '.join(palavras_decodificadas))
