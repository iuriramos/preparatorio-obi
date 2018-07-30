WEIGHT = 8
N = int(input())
pesos = [int(peso) for peso in input().split()]

def eh_possivel(pesos):
    prev = 0
    for curr in pesos:
        if curr - prev > WEIGHT:
            return False
        prev = curr
    return True
    '''
    pesos = [0] + pesos
    for i in range(len(pesos)-1):
        if pesos[i+1] - pesos[i] > WEIGHT:
            return False
    return True
    '''
    
if eh_possivel(pesos):
    print('S')
else:
    print('N')
