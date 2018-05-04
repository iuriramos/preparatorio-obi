N = int(input())
fita = input().split()
fita = [int(cor) for cor in fita]

index = 0
while index < N and fita[index] == -1:
    index += 1
while index < N:
    if fita[index] != 0:
        fita[index] = fita[index-1] + 1    
    index += 1

index = N-1
while index >= 0 and fita[index] != 0:
    index -= 1
while index >= 0:
    if fita[index] == -1:
        fita[index] = fita[index+1] + 1
    elif fita[index] != 0:
        fita[index] = min(fita[index], fita[index+1] + 1)
    index -= 1
# transforme a lista de inteiros para uma lista de strings antes
print(' '.join([str(cor) for cor in fita])) 

