a = float(input())
b = float(input())
c = float(input())

A = max(a, b, c) # maior
B = max(min(a, b), min(b, c), min(a, c)) # segundo maior
C = min(a, b, c) # menor
# C, B, A = sorted([a, b, c])

if A >= B + C:
    print ('NAO FORMA TRIANGULO')
elif A*A == B*B + C*C:
    print ('TRIANGULO RETANGULO')
elif A == B == C:
    print ('TRIANGULO EQUILATERO')
elif A == B or B == C:
    print ('TRIANGULO ISOSCELES')
else:
    print ('TRIANGULO ACUTANGULO OU OBTUSANGULO')
