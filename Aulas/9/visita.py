'''https://olimpiada.ic.unicamp.br/static/extras/obi2017/provas/ProvaOBI2017_f3p1.pdf'''

N, A, B = input().split()
N, A, B = int(N), int(A), int(B)

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    P, Q, D = input().split()
    P, Q, D = int(P), int(Q), int(D)
    graph[P].append((Q, D))
    graph[Q].append((P, D))

def distance_to_target(parent, node, target):
    if node == target:
        return 0
    for neigh, cost in graph[node]:
        if neigh != parent:
            dist_from_neigh_to_target = distance_to_target(node, neigh, target)
            if dist_from_neigh_to_target != -1:
                return cost + dist_from_neigh_to_target # cost = dist_from_node_to_neigh
    return -1

def distance_to_target2(node, target, visited):
    if node == target:
        return 0
    for neigh, cost in graph[node]:
        if neigh not in visited:
            visited.add(neigh)
            dist_from_neigh_to_target = distance_to_target2(neigh, target, visited)
            if dist_from_neigh_to_target != -1:
                return cost + dist_from_neigh_to_target
    return -1

print(distance_to_target(-1, A, B))

# visited = set()
# visited.add(A)
# print(distance_to_target2(A, B, visited))
