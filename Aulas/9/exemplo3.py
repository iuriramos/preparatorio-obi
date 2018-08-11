'''
4 4
0 1 1
1 2 2
1 3 3
3 2 4
# matriz de adj.
# *lista de adj.
'''
N, M = input().split() # nodes, edges
N, M = int(N), int(M)

# adj list
graph = []
for i in range(N):
    graph.append([])
    
# graph = [[] for j in range(N)] 

# grafo nao direcionado com pesos
for i in range(M): # [[], [3], [3], [2, 1
    origin, dest, weight = [int(node) for node in input().split()]
    graph[origin].append((dest, weight))
    graph[dest].append((origin, weight))

'''
# grafo não direcionado
for i in range(M): # [[], [3], [3], [2, 1
    origin, dest = [int(node) for node in input().split()]
    graph[origin].append(dest)
    graph[dest].append(origin)
''' 
print(graph)


