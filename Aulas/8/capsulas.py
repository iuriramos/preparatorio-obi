N, F = [int(num) for num in input().split()]
ciclos = [int(num) for num in input().split()]

def capsulas_naive(ciclos, min_moedas):
    dia = 0
    moedas = 0
    while moedas < min_moedas:
        dia += 1
        moedas += moedas_geradas_por_dia(ciclos, dia)    
    return dia
    
def moedas_geradas_por_dia(ciclos, dia):
    moedas = 0
    for ciclo in ciclos:
        if dia % ciclo == 0:
            moedas += 1
    return moedas
        
print(capsulas_naive(ciclos, F))


