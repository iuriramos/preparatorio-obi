# coding: utf-8
# python2 e python3
array = [0, 1, 2, 3]
array2 = array[:]
array2
# python3
array3 = array.copy()
array3
import antigravity
'ola ' + 'ola '
'ola ' * 5 
N = 3
'ola ' * N
[0] * N
[1] * N
[1, 2, 3, ] * N
[10] * N
[10 for i in range(N)] 
L = [1, 2, 3, 4]
range(4) # 0, 1, 2, 3
for i in range(4):
    print (i)
    
for i in range(10, 21):
    print (i) 
    
L = [1, 2, 3, 4]
for i in L:
    print (i)
    
range(2, 5) # [2, 3, 4]
for i in L:
    print (i)
    
l = [100, 200, 300, 400]
for i in l:
    print (i)
    
N = len(l)
N
l
for i in range(N):
    print (i)
    
for i in range(N):
    print (i, l[i]) 
    
    
for i, num in enumerate(l):
    print (i, num)
    
for i in range(N):
    print (i, l[i]) 
    
    
for n in l:
    print (n)
    
l
l.sort()
l
sorted(l)
ll = l.sort()
ll
ll = sorted(l)
l = [4, 3, 2, 1]
ll = sorted(l) 
ll
ll[0] = 0
ll
l
l
l.sort() 
l
l.reverse()
l
l.sort(), l.reverse()
l
l.sort()
l.reverse()
l
l.sort(reverse=True) 
l
l
l.pop(-1) 
l
l.pop(0)
l
c = {1, 2, 3, }
c
c.add(4)
c
c.remove(3)
c
c = set()
c.add(1)
c
c.add(1)
c
import numpy as np
l = list(range(10000)) 
l[:10] 
ll = list(range(1000))
ll[:20]
import random
random.shuffle(l)
random.shuffle(ll)
l[:10]
ll[:20]
count = 0
for num1 in ll: # 1000
    for num2 in l: # 10000
        if num1 == num2:
            count += 1
            
ll = list(range(100000))
len(l)
count = 0
for num1 in ll: # 1000
    for num2 in l: # 10000
        if num1 == num2:
            count += 1
            
count
len(l)
s = set(l) 
count = 0
for num1 in ll: # 1000
    if num1 in s:
        count += 1
        
count
get_ipython().magic('save comandos.py ~0/')
