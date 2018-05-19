#-------------------------------------------------------------------------------------------
#basquete.py3
'''
D = int(input())

if D <= 800:
    print(1)
elif 800 < D <= 1400:
    print(2)
elif 1400 < D <= 2000:
    print(3)
'''

#-------------------------------------------------------------------------------------------
#album.py3

i = 1

N = int(input())

L = [0] * N

M = int(input())

while i <= M:
    A = int(input())    
    A -= 1 # A = A -1
    L[A] += 1 # L[A] = L[A]+ 1
    i += 1 # i = i + 1

count = 0 # 3

for num in L: # 3,'0,1,0,0,5
    if num == 0:
        count += 1

print(count)

# print(L.count(0))

'''    
# L = [3, 0, 1, 0, 0, 5]

for i in range(N): # 0,1,..,N-1
    if L[i] == 0:
        print (i+1, end=' ')

'''


