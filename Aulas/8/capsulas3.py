'''Versao Mais Otimizada'''

N, F = [int(num) for num in input().split()]
ciclos = [int(num) for num in input().split()]
    
def capsulas(ciclos, min_moedas):
    ciclos = criar_tabela_frequencia(ciclos) # pré-processamento
    start, end = 0, 10**8
    while start < end:
        mid = (start + end) // 2
        moedas = total_moedas_geradas(ciclos, mid)
        if moedas >= min_moedas:
            end = mid
        else: # moedas < min_moedas:
            start = mid + 1
    return start # start == end ao final do loop
    
def criar_tabela_frequencia(ciclos):
    '''Otimização para casos onde ciclo possui muitos elementos repetidos'''
    frequencia = {} # dicionário: item >> ocorrências
    for ciclo in ciclos:
        if ciclo not in frequencia:
            frequencia[ciclo] = 1
        else:
            frequencia[ciclo] += 1
    return frequencia
        
def total_moedas_geradas(ciclos, dia):
    '''Total moedas geradas até determinado dia'''
    moedas = 0
    for ciclo, ocorrencia in ciclos.items(): # ciclo, ocorrencia == chave, valor (do dicionário)
        moedas += (dia // ciclo) * ocorrencia
    return moedas

print(capsulas(ciclos, F))

