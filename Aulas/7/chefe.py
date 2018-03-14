# troca de vértices
def troca(i, j):
    idades[i], idades[j] = idades[j], idades[i] # forma pythonica para trocar as idades

# percorre
def min_idade(row, adj):
    # visitado = [False, False, False, False]
    visitado = [False] * N # [False, False, ...., False] N vezes
    minimo = 101
    # for col in (0, 1, 2, 3): # coluna da matriz de adj.
    for col in range(N):
        if adj[row][col] == 1:
            idade = _min_idade(row, adj, visitado)
            minimo = min(minimo, idade)
    return minimo if minimo <= 100 else '*'
    
def _min_idade(row, adj, visitado):
    visitado[row] = True
    minimo = idades[row]
    # for col in (0, 1, 2, 3):
    for col in range(N):
        if adj[row][col] == 1:
            if visitado[col] == False:
                idade = _min_idade(col, adj, visitado)
                minimo = min(minimo, idade)  
    return minimo
    
if __name__ == '__main__':
    N = 4 # pessoas
    adj = [[0, 1, 1, 0], 
           [0, 0, 0, 1],
           [0, 1, 0, 0],
           [0, 0, 0, 0]]
    idades = [20, 20, 19, 18]
            
    print(min_idade(0, adj))
    troca(0, 3)
    print(min_idade(3, adj))
