import time

N = int(input())

lista = [0] * N # 10k

start = time.time()
while len(lista) > 0: # while lista:
    lista.pop(-1)
end = time.time()

print('Tempo Necessário tirando do final: ', end-start)

lista = [0] * N # 10k

start = time.time()
while len(lista) > 0: # while lista:
    lista.pop(0)
end = time.time()

print('Tempo Necessário tirando do início: ', end-start)
