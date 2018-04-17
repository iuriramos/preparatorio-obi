N = int(input())
maior = float('-inf')
menor = float('inf')
teste = 1

while teste <= N:
    entrada = input() # '3 4'
    X, Y = entrada.split() # ['3', '4']
    X, Y = int(X), int(Y)

    if X % 2 == 0:
        X = X + 1
    # (X + 0) + (X+2) + (X+4) + ...

    soma = 0 # X=3, Y=2 >>> X + (X + 2) = 3 + 5 = 8
    num = X # X+2, X+4, ....
    contador = 1 # 0, ..., Y

    while contador <= Y:
        soma = soma + num # soma = 8
        num = num + 2 # num = 7
        contador = contador + 1 # contador = 3
        # print('soma=', soma, 'num=', num, 'contador=', contador)
    print (soma) # 8
    
    # registrar maior e menor somas
    if soma < menor:
        menor = soma
    if soma > maior:
        maior = soma

    teste = teste + 1
    
# imprimir maior e menor somas
print(maior)
print(menor)
