'''TODO: Solução Trivial utilizando djkstra
https://olimpiada.ic.unicamp.br/static/extras/obi2017/provas/ProvaOBI2017_f2p2.pdf
'''
import heapq

N, M = input().split()
N, M = int(N), int(M)

graph = [[] for _ in range(N+1)] 

for _ in range(M):
    origin, dest, weight = [int(n) for n in input().split()]
    origin, dest = origin, dest
    graph[origin].append((dest, weight))
    graph[dest].append((origin, weight))
    
def min_distance(origin, destination):
    distancemap = [float('infinity')] * len(graph)
    distancemap[origin] = 0
    visited = [False] * len(graph)
    
    while has_unvisited_elements(visited):
        node = pop_node_with_min_distance(distancemap, visited)
        if node == destination:
            return distancemap[node]
        update_distancemap_with_neighbors_of_node(node, distancemap)
    return -1
    
def has_unvisited_elements(visited):
    return not all(visited[1:]) 
    
def pop_node_with_min_distance(distancemap, visited):
    min_node, min_distance = None, float('infinity')
    for node in range(len(graph)):
        distance_node = distancemap[node]
        if not visited[node] and distance_node <= min_distance:
            min_node, min_distance = node, distance_node
    visited[min_node] = True
    return min_node
            
def update_distancemap_with_neighbors_of_node(node, distancemap):
    for neigh, weight in graph[node]:
        new_distance = distancemap[node] + weight
        if new_distance < distancemap[neigh]:
            distancemap[neigh] = new_distance
            
    
def min_distance2(origin, destination):
    distancemap = {}
    distancemap[origin] = 0
    heap = []
    heappush(heap, origin, 0)
    
    while heap:
        distance, node = heappop(heap)
        if node == destination:
            return distancemap[node]
        update_distancemap_with_neighbors_of_node2(node, heap, distancemap)
    return -1
   
def update_distancemap_with_neighbors_of_node2(node, heap, distancemap):
    for neigh, weight in graph[node]:
        new_distance = distancemap[node] + weight
        if neigh not in distancemap or new_distance < distancemap[neigh]:
            distancemap[neigh] = new_distance
            heappush(heap, neigh, new_distance)

 
def min_distance3(origin, destination):
    heap = []
    distancemap = {origin: 0}
    heappush(heap, origin, priority=0)
    while heap:
        distance, node = heappop(heap)
        if node == destination:
            return distance
        for neighbor, weight in graph[node]:
            new_distance = distance + weight
            if neighbor not in distancemap or new_distance < distancemap[neighbor]:
                distancemap[neighbor] = new_distance
                heappush(heap, neighbor, new_distance)
    return -1 

def heappush(heap, item, priority):
    heapq.heappush(heap, (priority, item))

def heappop(heap):
    return heapq.heappop(heap)


print(min_distance(origin=1, destination=N))


