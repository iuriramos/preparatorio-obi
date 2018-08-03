'''Versao Nao Otimizada'''

N, M = input().split()
N, M = int(N), int(M)
rowi, coli = input().split()
rowi, coli = int(rowi)-1, int(coli)-1
rowf, colf = input().split()
rowf, colf = int(rowf)-1, int(colf)-1

grid = [['.'] * M for _ in range(N)]
for row in range(N):
    for col in range(M):
        if row % 2 == 1 and col % 2 == 1: # blocked cell
            grid[row][col] = '#'

# maximum path between (rowi, coli) and (rowf, colf)
def max_path(grid, row, col, rowf, colf):
    # (row, col) is final position
    if (row, col) == (rowf, colf):
        return 0
    dist = 0
    # mark cell as visited, avoid cycles
    grid[row][col] = '#' # can replace '#' by any other token: 'v', '@', etc.
    # visted neighbors
    for drow, dcol in ((-1, 0), (0, -1), (0, 1), (1, 0)):
        nrow, ncol = row + drow, col + dcol
        if check_valid_cell(grid, nrow, ncol): # valid next position
            dist = max(dist, 1 + max_path(grid, nrow, ncol, rowf, colf))
    # unmark visited cell
    grid[row][col] = '.'
    return dist

def check_valid_cell(grid, row, col):
    if row < 0 or row >= N or col < 0 or col >= M: # out of bounds
        return False
    return grid[row][col] == '.'

# max_path returns `maximum path`, which contains `maximum path + 1` cells
print(max_path(grid, rowi, coli, rowf, colf) + 1) 
