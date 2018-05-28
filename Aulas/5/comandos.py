# coding: utf-8
linhas = ['ana', 'beatriz', 'clara']
linhas
# lista de strings >>> string
' '.join(linhas) 
'--'.join(linhas)
s = ''.join(linhas)
s
s = ' '.join(linhas)
# string >>> lista de strings
s.split()
s = '--'.join(linhas)
s
s.split()
s.split('--')  
s = '1 2 3 4'
l = s.split()
l
[1, 2, 3, 4] 
nums = [] 
l
for num in l:
    print( int(num) )
     
for num in l:
    print( int(num) + 1 ) 
    
     
l
for num in l:
    print( num + 1 ) 
    
    
     
nums = []
for num in l:
    n = int(num)
    nums.append(n)
     
    
     
nums
nums = [int(num) for num in l] 
s
list(s)
s = 'cão'
list(s) 
l = list(s)
l
l[2] = 'a'
l
''.join(l)
l = [1, 2, 2]
l.remove(2)
l
l.remove(2) 
l
l.remove(2)
s = 'ola'
for c in s: # c = 'a'
    print(c) 
    
l = [1,2, 3, ]
l
l.index(3)
d = {} # dict()
d
d['a'] = 1
d
d['b'] = 1
d
d['a'] 
d['b'] 
{} # dict
get_ipython().magic('save comandos.py ~0/')
