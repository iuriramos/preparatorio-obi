'''Versao Otimizada'''

from tree import Tree
# sweeping line

N = int(input())

rooms = []
for _ in range(N):
    room = [int(num) for num in input().split()]
    rooms.append(room)

# total routers
wifis = 0
    
# reduce room into two vertical edges (x1, y2, y1) and (x2, y2, y1)
entries = []
for x1, y1, x2, y2 in rooms:
    entries.append((x1, y2, y1)) # y2 < y1
    entries.append((x2, y2, y1))

# sort them
entries.sort()

# tree datastucture
tree = Tree()

# insert first entry in order to have returned value for lower_bound
first_entry = entries[0]
x, y1, y2 = first_entry
tree.set(y1, 0)
tree.set(y2, 1)

for x, y1, y2 in entries[1:]:
    if tree.exists(y1) and tree.exists(y2):
        if tree.get(y1) == 0:
            wifis += 1
        tree.remove(y1)
        tree.remove(y2)
    else:
        y0 = tree.previous(y1)
        tree.set(y0, 1)
        # if tree.get(y0) == 0:
        #     tree.set(y0, 1)
        tree.set(y1, 0)
        tree.set(y2, 1)

print(wifis)


