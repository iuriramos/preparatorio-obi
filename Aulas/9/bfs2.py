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
    came_from = {} # mapeia 'node' em 'parent node' (algoritmo primeiro visitou 'parent node', e de lá visitou 'node' 
    came_from[start] = None # 'start' não possui 'parent node'
    
    while len(queue) > 0:
        node = queue.popleft() # retira 1o elemento da fila
        if node == end:
            path = find_path_between_nodes(start, end, came_from)
            return path # retorna caminho
        for neigh in adj[node]: # percorre todos os vizinhos de node
            if neigh not in came_from: # neigh não foi visitado
                came_from[neigh] = node # 'node' como pai de 'neigh'
                queue.append(neigh) # e adiciona neigh na fila
    return [] # não existe caminho entre start e end

def find_path_between_nodes(start, end, came_from):   
    rev_path = []
    node = end
    while node != start:
        rev_path.append(node)
        node = came_from[node]
    rev_path.append(start)
    rev_path.reverse()
    return rev_path
         
start, end = input().split()
start, end = int(start), int(end)
          
print('caminho entre', start, 'e', end)  
print(bfs(start, end))

