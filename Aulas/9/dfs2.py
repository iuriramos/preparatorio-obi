adj = [
    [4, 2, 1], # 0
    [0, 2],    # 1
    [0, 1, 3], # 2
    [2],       # 3
    [0],       # 4
    [],        # 5
]

def dfs(node, end, came_from):
    if node == end:
        return True
    for neigh in adj[node]:
        if neigh not in came_from:
            came_from[neigh] = node
            if dfs(neigh, end, came_from):
                return True
    return False
    
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

came_from = {}
came_from[start] = None

print('caminho entre', start, 'e', end)
found = dfs(start, end, came_from) # depth first search
if found:
    path = find_path_between_nodes(start, end, came_from)
    print(path) 
else:
    print([])
