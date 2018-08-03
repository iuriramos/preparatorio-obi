'''Versao Otimizada'''

N, F = [int(num) for num in input().split()]
ciclos = [int(num) for num in input().split()]

def capsulas(ciclos, min_moedas):
    start, end = 0, 10**8
    while start < end:
        mid = (start + end) // 2
        moedas = total_moedas_geradas(ciclos, mid)
        if moedas == min_moedas:
            end = mid
        elif moedas < min_moedas:
            start = mid + 1
        else: # moedas > min_moedas
            end = mid
    return start # start == end ao final do loop
    
def capsulas2(ciclos, min_moedas):
    start, end = 0, 10**8
    while start < end:
        mid = (start + end) // 2
        moedas = total_moedas_geradas(ciclos, mid)
        if moedas >= min_moedas:
            end = mid
        else: # moedas < min_moedas:
            start = mid + 1
    return start # start == end ao final do loop
        
def total_moedas_geradas(ciclos, dia):
    '''Total moedas geradas até determinado dia'''
    moedas = 0
    for ciclo in ciclos:
        moedas += (dia // ciclo)
    return moedas

print(capsulas(ciclos, F))
# print(capsulas2(ciclos, F))

