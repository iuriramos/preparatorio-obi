'''
Recebe números como input, 
retorna a frequência de cada número, que variam de 0..100.
'''

nums = [int(num) for num in input().split()]

def monta_tabela_freq(nums):
    tabela_freq = [0] * 101 # [0, 2, 3, ..., 0(101th)]
    # monta tabela de frequencia
    for num in nums:
        tabela_freq[num] += 1
    # mostra tabela de frequencia
    for num in range(len(tabela_freq)):
        if tabela_freq[num] > 0:
            print(num, ':', tabela_freq[num])
        
# monta_tabela_freq(nums)
        
def calcula_tabela_freq2(nums):
    tabela_freq = {} # {2: 3, 3: 2}
    for num in nums: # 2, 2, 2, 3, 3, '
        if num not in tabela_freq:
            tabela_freq[num] = 0
        tabela_freq[num] = tabela_freq[num] + 1
    print (tabela_freq)

def calcula_tabela_freq3(nums):
    tabela_freq = {} # {2: 2}
    for num in nums: # 2, '2, 2, 3, 3,
        tabela_freq[num] = tabela_freq.get(num, 0) + 1
    print (tabela_freq)

import collections

def calcula_tabela_freq4(nums):
    counter = collections.Counter(nums)    
    print(counter)
    # print(1 not in counter)
    counter[5] += 2
    print(counter)
    
calcula_tabela_freq4(nums)  
     
def cria_dicionario():
    '''Vantagens: busca rápida; associar chave >> valor
    
    chave: int, string, tuple
    valor: int, string, tuple, list, dict, set, 
    '''
    d = {}
    d = {'a': 100, 1: 'aaaaa', 'b': 2}
    #d = dict(1=2, 2=3)
    print(1 in d) # operação de 'pertence'
    print(3 not in d) # True
    print(d['a'])
    d[3] = 1000
    print(d.get(1, ''))
    del d[1]
    print(d.get(1, 'bbbbb'))
    
def cria_set():
    #s = set()
    #s = {1, 2, 3, 4}
    s = set([1, 2, 3, 4])
    print (1 in s) # True
    print (2 not in s) # False
    print(s)
    s.add(5)
    print('apos adicionar 5', s)
    s.remove(4)
    print('apos remover 4', s)

# cria_set()  


