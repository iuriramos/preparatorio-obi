adj = [
    [4, 2, 1], # 0
    [0, 2],    # 1
    [0, 1, 3], # 2
    [2],       # 3
    [0],       # 4
    [],        # 5
]
visitado = [False for i in range(6)]

def dfs(start, end):
    if start == end:
        return True
    for neigh in adj[start]: # 0, 1, 3
        if visitado[neigh] == False:
            came_from[neigh] = start
            visitado[neigh] = True
            if dfs(neigh, end) == True:
                return True
    return False
    
start, end = [int(num) for num in input().split()]
visitado[start] = True

came_from = {} # chave(node): valor(parent)
came_from[start] = -1

found = dfs(start, end) # depth first search

if found:
    print('Encontrei')
    path = [end]
    while True:
        node = path[-1]
        pnode = came_from[node]
        if pnode == -1:
            break
        path.append(pnode)
    path.reverse()
    print(path)
    
else:
    print('Não Encontrei')

