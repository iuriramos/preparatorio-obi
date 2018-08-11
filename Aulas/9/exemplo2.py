'''
4 4
0 1
1 2
1 3
3 2
# matriz de adj.
# *lista de adj.
'''
N, M = input().split() # nodes, edges
N, M = int(N), int(M)

# NxN matrix
graph = []
for i in range(N):
    row = [0 for j in range(N)]
    graph.append(row)
    
# graph = [[0 for i in range(N)] for j in range(N)] 

# grafo não direcionado
for i in range(M):
    origin, dest = [int(node) for node in input().split()]
    graph[origin][dest] = 1
    graph[dest][origin] = 1
    
print(graph)


