from collections import deque

adj = [
    [4, 2, 1], # 0
    [0, 2],    # 1
    [0, 1, 3], # 2
    [2],       # 3
    [0],       # 4
    [],        # 5
]
visitado = [False for i in range(6)]

start, end = [int(num) for num in input().split()]

fila = deque([start]) # []
visitado[start] = True # [T,T,T,T,T,F]
found = False
came_from = {} # chave(node): valor(parent)
came_from[start] = -1

while len(fila) > 0:
    node = fila.popleft() # 3
    if node == end:
        found = True
        break
    for neigh in adj[node]: # [0, 1, 3']
        if visitado[neigh] == False:
            came_from[neigh] = node
            visitado[neigh] = True
            fila.append(neigh)
            
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









