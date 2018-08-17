'''https://olimpiada.ic.unicamp.br/static/extras/obi2017/provas/ProvaOBI2017_f2p1.pdf'''

N, M = input().split()
N, M = int(N), int(M)

colormap = [0] * (N+1)
graph = [[] for _ in range(N+1)]

def paint(node, dest, color, visited):
    if node == dest:
        colormap[node] = color
        return True 
    for neigh in graph[node]:
        if neigh not in visited:
            visited.add(neigh)
            if paint(neigh, dest, color, visited):
                colormap[node] = color
                return True
    return False 

for _ in range(N-1):
    P, Q = [int(num) for num in input().split()]
    graph[P].append(Q)
    graph[Q].append(P)

for _ in range(M):
    origin, dest, color = [int(num) for num in input().split()]
    visited = set()
    visited.add(origin)
    paint(origin, dest, color, visited) # include visited here

print(*colormap[1:])
