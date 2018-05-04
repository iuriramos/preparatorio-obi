N, M = input().split()
N, M = int(N), int(M) # importante! transformar em inteiros
pinos = input().split()
pinos = [int(pino) for pino in pinos] # importante! transformar em inteiros
total_movimentos = 0
for i in range(N-1):
    movimentos = M - pinos[i]
    pinos[i+1] += movimentos
    total_movimentos += abs(movimentos)
    # ultimo pino
    # total_movimentos += abs(pinos[N-1] - altura) # indica possibilidade ou nao
print(total_movimentos)
