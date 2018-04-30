# coding: utf-8
a = input() 
a
a = int(input())
a
[1, 2, 3, 4, 5]
lista = [1, 2, 3, 4, 5]
lista
type(lista)
lista = [0] * 1 
lista
lista = [0] * 2 
lista
lista = [0] * 10
lista
lista = [5] * 10
lista
lista = [2, 5] * 10
lista
lista = [2, 5] * 5
lista
len(lista) 
nomes = ['ana', 'beatriz', 'carlos']
nomes
len(nomes)
nomes[0] 
nomes[1]
nomes[2]
nomes
nomes[len(nomes)-1] 
N = len(nomes)
N
N-1
nomes[N-1]
nomes
nomes[-1]
nomes[-2] 
nomes[-3]
nomes[-4] 
nomes
N
nomes[3]
lista
N = len(nomes)
nomes
nomes[N-1]
nomes[N-2]
N = len(nomes)
N-1
N-2
lista
lista = list(range(10)) 
lista
lista[0: 2] 
lista = [1, 2, 3, 4, 5, 6]
lista[0: 2]
lista[0: 3]
lista[0: 4]
lista[1: 4]
lista
lista[-1:-4] 
lista[0:2:1]
lista[0:4:2] 
lista
lista[-3:] 
lista[-1:-4:-1] 
lista
lista[0:2]
lista[:2] 
lista[-2:]
lista
lista[-1]
lista[2:] 
lista[3:] 
lista[-3:]
lista[:]
lista2 = lista
lista
lista2
lista[0] = 0
lista
lista2
a = 5
b = 6
a = 5
b = a
a
b
a = 6
b
lista
lista[:] 
lista2 = lista[:]
lista2
lista
lista[0] = 1
lista
lista2
lista3 = lista
lista3
lista
lista[0] = 0
lista
lista3
lista3[1] = 1
lista3
lista
lista2
lista[1] = 0
lista[1]
lista[1:3]
lista
lista = list(range(10))
lista
soma = 0
for num in lista:
    soma = soma + num 
    
for num in lista:
    print (num)
    soma = soma + num 
    
lista
for num in lista:
    soma = soma + num 
    
soma
lista
lista.append(10)
lista
lista.insert(0, -1)
lista
lista
lista
alvo = 5
N = len(lista) 
N
for i in range(N): # 0, 1, ..., N-1
    num = lista[i]
    if num == alvo:
        print (i)
        
for num in lista:
    if num == alvo:
        print('alvo está na lista')
        
for i, num in enumerate(lista):
    if num == alvo:
        print(i)
        
for i, num in enumerate(lista):
    print(i , num)
    
        
lista
for i in range(N): # 0, 1, ..., N-1
    num = lista[i]
    if num == alvo:
        print (i)
        
help(list)
lista.index(alvo)
lista.count(alvo)
lista[0] = alvo
lista
lista.count(alvo)
lista.index(alvo)
for i, num in enumerate(lista):
    print(i , num)
    
        
i = 0 # 0, 1, .. , N-1
while i < N:
    num = lista[i]
    if num == alvo:
        print (i)
    i += 1
    
produto = 1
for num in lista:
    produto = produto * num
    
produto
lista = [0, 1, 2, 3, 4, 5, 6]
i = 0
N = len(lista)
N
soma = 0
while i < N:
    num = lista[i]
    if i % 2 == 0:
        soma = soma + num
    
while i < N:
    num = lista[i]
    if i % 2 == 0:
        soma = soma + num
    i += 1
    
soma = 0
while i < N:
    num = lista[i]
    if i % 2 == 0:
        soma = soma + num
    i += 1
    
soma
lista
i
soma = 0
i = 0
N = len(lista)
while i < N:
    num = lista[i]
    if i % 2 == 0:
        soma = soma + num
    i += 1
    
soma
lista
lista[::2] 
sum(lista[::2])
soma = 0
for num in lista[::2]:
    soma = soma + num
    
soma
lista = [1]
lista = [2, 3]
lista = [1] * 5
lista
lista + lista2
lista = [1, 2, 3]
lista2 = [4, 5 ,6]
lista + lista2
lista
lista * 3
lista = [10, 7, 2, 3, 1]
sorted(lista)
lista
lista2 = sorted(lista)
lista2
lista
lista.sort() 
lista
lista.reverse()
lista
lista.sort(reverse=True) 
lisgta
lista
max(lista)
min(lista)
lista = [1, 2, 3, 4]
[2, 4, 6, 8]
lista2 = []
for num in lista:
    new_num = 2*num
    lista2.append(new_num)
    
lista2
lista3 = [2*num for num in lista] 
lista3
nome = 'iuri'
l = ['i', 'u', 'r', 'i']
nome
l
nome[0] 
l[0] 
for ch in l:
    print (ch) 
    
for ch in nome:
    print (ch)
    
nome
l
len(nome)
len(l)
l
l[1] = 'o'
l
nome[1] = 'o'
nome
l
sorted(l)
sorted(l)
nome
nome[1] = 'o'
nome
nome = 'ana maria'
nome.split()
nome = 'ana'
['a', 'n', 'a']
list(nome)
lista_nome = list(nome)
lista_nome
lista_nome = [ch for ch in nome] 
lista_nome
lista_nome[1] = 'o'
lista_nome
lista = [[1, 2, 3], [4, 5, 6]]
lista[1][2]
lista[1][2] = 7
lista
lista2 = lista.copy()
lista
lista2
lista2 = lista[:]
lista2
s = 'ana maria'
s.split()
lista = s.split()
lista
' '.join(lista) 
''.join(lista) 
'--'.join(lista) 
lista
lista[0]
l = list(lista[0])
l
l[0: :2] 
l[1: :2] 
l
get_ipython().magic('save ~0 códigos.py/')
get_ipython().magic('save códigos.py ~0/')
