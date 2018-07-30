import heapq # priority queue / lista de prioridade

L, C, K = [int(num) for num in input().split()]

grid = []
for _ in range(L):
    row = [int(num) for num in input().split()]
    grid.append(row)
    

def min_distance(grid, rowf, colf):
    '''Minimum distance from 0, 0 to rowf, colf (dijkstra's algorithm)'''
    heap = []
    rowi, coli = 0, 0 # initial positions
    time = 0 # grid[rowi][coli] == 0
    push_heap(heap, priority=time, item=(rowi, coli))
    came_from = {}
    came_from[rowi, coli] = None
    
    while heap:
        time, (row, col) = pop_heap(heap)
        if (row, col) == (rowf, colf):
            return time
        for drow, dcol in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            nrow, ncol = row + drow, col + dcol
            feasible_move(grid, heap, came_from, row, col, nrow, ncol, time)
            
    return -1

def feasible_move(grid, heap, came_from, row, col, nrow, ncol, time):
    if nrow < 0 or nrow >= L or ncol < 0 or ncol >= C:
        return # invalid next position
    if (nrow, ncol) in came_from:
        return # has already visited next position
    clock, nclock = grid[row][col], grid[nrow][ncol]
    if nclock == -1: # can wait in next position
        came_from[nrow, ncol] = (row, col)
        push_heap(heap, priority=time+1, item=(nrow, ncol))
    else: # cannot wait in next position
        if clock == -1: # can wait in current position
            came_from[nrow, ncol] = (row, col)
            ntime = time_to_wait(time, nclock)
            push_heap(heap, priority=ntime, item=(nrow, ncol))
        elif (clock + 1) % K == nclock: # cannot wait in current position, but can move to next position
            came_from[nrow, ncol] = (row, col)
            push_heap(heap, priority=time+1, item=(nrow, ncol))
    
def time_to_wait(time, nclock):
    k_time = time % K
    if k_time < nclock:
        return time + (nclock - k_time)
    else: 
        return time + (K - k_time) + nclock
    
def push_heap(heap, priority, item):
    '''Insert item with certain priority'''
    heapq.heappush(heap, (priority, item))
    
def pop_heap(heap):
    '''Return item with minimum priority'''
    priority, item = heapq.heappop(heap)
    return priority, item
    
print(min_distance(grid, rowf=L-1, colf=C-1))
