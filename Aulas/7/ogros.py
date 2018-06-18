N, M = input().split()
faixas = [int(faixa) for faixa in input().split()]
prems = [int(prem) for prem in input().split()]
forcas = [int(forca) for forca in input().split()]

def get_resultado(faixas, prems, forca):
    lo, hi = 0, len(faixas)-1
    while lo < hi:
        mid = (lo+hi+1)//2
        val = faixas[mid]
        if val <= forca:
            lo = mid
        else: # val > forca
            hi = mid-1
    return prems[lo]
            

resultados = []
faixas.insert(0, 0)

for forca in forcas:
    resultado = get_resultado(faixas, prems, forca)
    resultados += [str(resultado)]
    
print(' '.join(resultados))
