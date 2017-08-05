def floyd_warshall(start, end):
    # Floyd Warshall
    # --------------
    # d_k(i, j) = c(i, j), k == 0
    # d_k(i, j) = min( d_k-1(i, j), d_k-1(i, k) + d_k-1(k, j) ), k > 0
    
    # fazer cópia de matrix
    distance = [[0] * N for _ in matrix]
    next_distance = [[0] * N for _ in matrix]
    for i in range(N):
        for j in range(N):
            distance[i][j] = matrix[i][j]
                
    for k in range(N):
        for i in range(N):
            for j in range(N):
                next_distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
        distance = next_distance
                
    return distance[start][end]
    
    
def floyd_warshall_simplificado(start, end):
    # Floyd Warshall
    # --------------
    # Para simplificar e otimizar a utilização de memória
    # provar que d_k(i, j) = min( d_k-1(i, j), d_k(i, k) + d_k(k, j) ) também é valido!
    
    # fazer cópia de matrix
    distance = [[0] * N for _ in matrix]
    for i in range(N):
        for j in range(N):
            distance[i][j] = matrix[i][j]
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
                
    return distance[start][end]
              
if __name__ == '__main__': 
    matrix = [ 
        [0, 1, 4], # 0
        [0, 0, 2], # 1
        [0, 0, 0]] # 2 

    N = len(matrix)
    print(floyd_warshall(0, 2))
    print(floyd_warshall_simplificado(0, 2))
