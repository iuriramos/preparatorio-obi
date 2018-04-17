# coding: utf-8
2
5
type(5)
6.7
type(6.7)
'olá mundo'
type('ola mundo')
4 == 2 + 2
2 + 4
2 * 6
6 // 2
7 / 2
7 % 2
8 % 2
print('Olá Mundo')
print('Olá Mundo', 'meu nome é', 'Iuri')
nome = 'Iuri'
print(nome)
print(nome)
nome = 'Lucas'
print(nome)
input()
numero = input()
numero
numero
numero -1
n = int(numero) 
n
type(n)
n-1
numero = input() 
numero
numero = input() 
numero
float(numero)
numero = float(numero)
numero
nome = 'Lucas'
if nome == 'Lucas':
    print('Olá Lucas')
else:
    print('Olá outra pessoa')
    
nome = 'Iuri'
if nome == 'Lucas':
    print('Olá Lucas')
else:
    print('Olá outra pessoa')
    
a = float()  
a
float(input())
a = float(input())
a
a = float()  
a
a = input()
a = float(a) 
[] 
type([])
[1, 2, 3, 4, 5] 
array = [5, 4, 3, 2, 1]
type(array)
array[0] 
array[3]
array[4] 
array
len(array) 
array[len(array)-1] 
array[len(array)-2] 
array[-1] 
array[-2]  
array[-5]
array
array
array.append(0) 
array
array.insert(0, 6) 
array
array.append(-1)
array
array.pop()
array
array.pop()
array
array.pop(0) 
array
array
sorted(array) 
array
array
array.sort() 
array
sorted(array) 
array_ordenado = sorted(array)
array_ordenado
a, b, c 
a, b, c = 1, 2, 3
a
b
c
sorted([a, b, c]) 
a, b, c = 1, 3, 2
sorted([a, b, c]) 
c, b, a = sorted([a, b, c]) 
c
b
c
a
inf = float('-inf') 
inf
menos_inf
menos_inf = float('-inf')
menos_inf
5 < menos_inf
-10000 <  menos_inf
5 >  menos_inf
5 >  menos_inf
max(2, 3, 5)
max([3, 4, 5, 6, 100]) 
max([])
0 / 0
i = 0
while i < 10:
    print(i)
    i = i + 1 
    
for i in [0, 1, 2, 3, 4, 5]:
    print(i)
    
for i in range(0, 100): # 0, 1, ..., 99
    print(i)
    
for i in range(0, 100, 2): # 0, 1, ..., 99
    print(i)
    
input()
int(input()) 
int('2'), int('3') 
'2 3'.split() 
texto = 'um texto qualquer'
texto.split()
a, b, c = texto.split()
a
b
c
a, b, c = ['um', 'texto', 'qualquer'] 
a
b
c
input() 
entrada = input()
entrada
X, Y = entrada.split() # ['2', '3'] 
X
Y
X = int(X)
Y = int(Y)
X, Y = int(X), int(Y) 
X
Y
int('2 3')
texto = '1:2:3'
texto.split(':') 
texto = '1a2a3'
texto.split('a') 
texto = '1   2        3'
texto.split() 
# split: str >>>> array
# join: array >>>> str
array = texto.split() 
array 
''.join(array)
' '.join(array)
'  '.join(array)
':'.join(array)
array = '1 3 4 5 5 6'.split()
array
len(array)
get_ipython().magic('save codigos.py ~0/')
