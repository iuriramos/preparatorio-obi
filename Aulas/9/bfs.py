from collections import deque

adj = [
    [4, 2, 1], # 0
    [0, 2],    # 1
    [0, 1, 3], # 2
    [2],       # 3
    [0],       # 4
    [],        # 5
]

def bfs(start, end):
    queue = deque([start]) # fila de processamento []
    visited = [False for i in range(6)]
    visited[start] = True 
    
    while len(queue) > 0:
        node = queue.popleft() # retira 1o elemento da fila
        if node == end:
            return True # end node encontrado
        for neigh in adj[node]: # percorre todos os vizinhos de node
            if not visited[neigh]: # neigh não foi visitado
                visited[neigh] = True # marca neigh como visitado
                queue.append(neigh) # e adiciona neigh na fila
    return False # end node não encontrado
            
start, end = input().split()
start, end = int(start), int(end)
            
if bfs(start, end):
    print('Encontrei')
else:
    print('Não Encontrei')
