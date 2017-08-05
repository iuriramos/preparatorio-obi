# troca de vértices
def troca(i, j):
    temp = Adj[i]
    Adj[i] = Adj[j]
    Adj[j] = temp # forma tradicional de troca
    Idade[i], Idade[j] = Idade[j], Idade[i] # forma pythonica para trocar as idades

# percorre
def min_idade(row, Adj):
    # visitado = [False, False, False, False]
    visitado = [False] * N # [False, False, ...., False] N vezes
    minimo = 101
    # for col in (0, 1, 2, 3): # coluna da matriz de adj.
    for col in range(N):
        if Adj[row][col] == 1:
            idade = _min_idade(row, Adj, visitado)
            minimo = min(minimo, idade)
    return minimo if minimo <= 100 else '*'
    
def _min_idade(row, Adj, visitado):
    minimo = Idade[row]
    # for col in (0, 1, 2, 3):
    for col in range(N):
        if Adj[row][col] == 1:
            if visitado[row] == False:
                visitado[row] = True
                idade = _min_idade(col, Adj, visitado)
                minimo = min(minimo, idade)  
    return minimo
    
if __name__ == '__main__':
    N = 4 # pessoas
    Adj = [[0, 1, 1, 0], 
           [0, 0, 0, 1],
           [0, 1, 0, 0],
           [0, 0, 0, 0]]
    Idade = [20, 20, 19, 18]
            
    print(min_idade(0, Adj))
    troca(0, 3)
    print(min_idade(3, Adj))
