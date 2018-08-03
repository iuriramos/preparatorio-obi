'''Versao Nao Otimizada'''

N, M = input().split()
N, M = int(N), int(M)
rowi, coli = input().split()
rowi, coli = int(rowi), int(coli)
rowf, colf = input().split()
rowf, colf = int(rowf), int(colf)

# avoid path with cycles*
visited = set()

# maximum path between (rowi, coli) and (rowf, colf)
def max_path(row, col, rowf, colf):
    # (row, col) is final position
    if (row, col) == (rowf, colf):
        return 0
    dist = 0
    # mark cell as visited, avoid cycles
    cell = (row, col)
    visited.add(cell)
    # visted neighbors
    for drow, dcol in ((-1, 0), (0, -1), (0, 1), (1, 0)):
        nrow, ncol = row + drow, col + dcol
        if check_valid_cell(nrow, ncol): # valid next position
            dist = max(dist, 1 + max_path(nrow, ncol, rowf, colf))
    # unmark visited cell
    visited.remove(cell)
    return dist

def check_valid_cell(row, col):
    if row < 1 or row > N or col < 1 or col > M: # out of bounds
        return False
    if row % 2 == 0 and col % 2 == 0: # blocked cell
        return False
    if (row, col) in visited: # visited cell
        return False
    return True # return true, otherwise


# max_path returns `maximum path`, which contains `maximum path + 1` cells
print(max_path(rowi, coli, rowf, colf) + 1) 
