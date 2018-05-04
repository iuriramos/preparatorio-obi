A = int(input())
B = int(input())
C = int(input())
H = int(input())
L = int(input())

# A <= B <= C
A, B, C = sorted([A, B, C]) # 20, 100, 80 >> 20, 80, 100
H, L = sorted([H, L]) # 100, 80 >> 80, 100

if A <= H and B <= L:
    print('S')
else: 
    print('N')
