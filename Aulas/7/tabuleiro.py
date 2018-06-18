N = int(input())
tabuleiro = []

for _ in range(N): # 0, 1, ..., N-1
    linha = input().split() # ['0', '0', '1', '0', '0','0']
    linha = [int(num) for num in linha] # [0, 0, 1, 0, 0, 0]
    tabuleiro.append(linha) # [ [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0], ... ]
    
for i in range(N):
    for j in range(N):
        # i >> linha, j >> coluna
        if tabuleiro[i][j] == 9:
            soma = tabuleiro[i-1][j] + tabuleiro[i][j-1] + tabuleiro[i-1][j-1]
            if soma < 2:
                tabuleiro[i][j] = 1
            else:
                tabuleiro[i][j] = 0

# retorna o último elemento
print(tabuleiro[-1][-1])
