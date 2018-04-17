num = input() 
num = int(num)
soma = 0
contador = 0
maior = float('-inf') # -INFINITO

while num != 0:
    # print('Antes:', 'num=', num, 'soma=', soma, 'contador=', contador, 'maior=', maior)
    soma = soma + num
    contador = contador + 1
    if num > maior:
        maior = num
    # print('Depois:', 'num=', num, 'soma=', soma, 'contador=', contador, 'maior=', maior)
    num = int(input())
    
# checar se usuario entrou com numero
if contador == 0:
    print(0)
    print(0)
    print(0)
else:
    print(contador)
    print(max(nums))
    print(round(soma / contador, 2)) 
