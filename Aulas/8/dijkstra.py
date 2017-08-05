def dijkstra(start, end):
    intree = [False] * N
    parent = [-1] * N
    distance = [INFINITE] * N
    
    node = start
    distance[start] = 0
    intree[start] = True
    
    while node != -1: #
        print(node)
        for next in range(N): # 0, 1, ..., N -1
            if matrix[node][next] > 0:
                new_dist = (distance[node] + matrix[node][next])
                if new_dist < distance[next]:
                    distance[next] = new_dist
                    parent[next] = node
            
        # pegar o próximo node
        node = -1
        min_dist = INFINITE
        for i in range(N):
            if (distance[i] < min_dist and
                 intree[i] == False):
                min_dist = distance[i]
                node = i
                        
        if node != -1:
            intree[node] = True
    
    path = [] # caminho mínimo
    node = end
    while node != -1:
        path.append(node)
        node = parent[node]
    path = list(reversed(path))
    return path, distance[end]
              
if __name__ == '__main__':  
    matrix = [ 
        [0, 1, 4], # 0
        [0, 0, 5], # 1
        [0, 0, 0]] # 2 

    N = len(matrix)
    INFINITE = 100
    print(dijkstra(0, 2))
