def bfs(start, end):
    parent = [-1] * N
    curr = [0] * N
    i = 0 # ponteiro para curr
    
    parent[start] = start
    curr[i] = start
    i += 1
    
    while i > 0:
        next = [0] * N
        j = 0
        for k in range(i): # 0, 1, 2, .., i -1
            node = curr[k] # inicialmente: start
            linha = matrix[node] # [0, 1, 1, 0]
            for l in range(N): 
                if linha[l] == 1:
                    if parent[l] == -1:
                        parent[l] = node
                        next[j] = l
                        j += 1
        curr = next
        i = j
    
    path = [] # caminho mínimo
    node = end
    while node != parent[node]:
        path.append(node)
        node = parent[node]
    path.append(start)
    return list(reversed(path))
   
if __name__ == '__main__':
    vertices = [0, 1, 2, 3]
    matrix = [ 
        [0, 1, 1, 0], # 0
        [0, 0, 0, 1], # 1
        [0, 1, 0, 0], # 2
        [0, 0, 0, 0]] # 3
    N = len(matrix)
    print('bfs(0, 3) = ', bfs(0, 3))
    print('bfs(2, 3) = ', bfs(2, 3))    
