M, N = input().split()
M, N = int(M), int(N)

dinheiro_recebido = [0 for i in range(N+1)]
total_dinheiros = 0

for i in range(M):
    X, V, Y = input().split()
    X, V, Y = int(X), int(V), int(Y)
    dinheiro_recebido[X] -= V
    dinheiro_recebido[Y] += V
    total_dinheiros += V

total_recebido = 0
for i in range(N+1):
    if dinheiro_recebido[i] > 0:
        total_recebido += dinheiro_recebido[i]

if total_recebido < total_dinheiros:
    print('S')
else:
    print('N')
print(total_recebido)
