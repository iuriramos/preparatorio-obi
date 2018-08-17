adj = [
    [4, 2, 1], # 0
    [0, 2],    # 1
    [0, 1, 3], # 2
    [2],       # 3
    [0],       # 4
    [],        # 5
]

def dfs(node, end, visited):
    if node == end:
        return True
    for neigh in adj[node]:
        if not visited[neigh]:
            visited[neigh] = True
            if dfs(neigh, end, visited):
                return True
    return False
    
start, end = input().split()
start, end = int(start), int(end)

visited = [False for i in range(6)]
visited[start] = True

if dfs(start, end, visited): # depth first search
    print('Encontrei')    
else:
    print('Não Encontrei')

