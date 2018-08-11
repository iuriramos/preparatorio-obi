import time
from collections import deque

N = int(input())

lista = [0] * N # 10k
queue = deque(lista)

start = time.time()
while len(queue) > 0: # while lista:
    queue.pop()
end = time.time()

print('Tempo Necessário tirando do final: ', end-start)

lista = [0] * N # 10k
queue = deque(lista)

start = time.time()
while len(queue) > 0: # while lista:
    queue.popleft()
end = time.time()

print('Tempo Necessário tirando do início: ', end-start)
