val = int(input())

c100 = val // 100
r100 = val % 100
c50 = r100 // 50
r50 = r100 % 50
c20 = r50 // 20
r20 = r50 % 20
c10 = r20 // 10
r10 = r20 % 10
c5 = r10 // 5
r5 = r10 % 5
c2 = r5 // 2
r2 = r5 % 2
c1 = r2

print(val)
print(c100, 'nota(s) de R$100,00')
print(c50, 'nota(s) de R$50,00')
print(c20, 'nota(s) de R$20,00')
print(c10, 'nota(s) de R$10,00')
print(c5, 'nota(s) de R$5,00')
print(c2, 'nota(s) de R$2,00')
print(c1, 'nota(s) de R$1,00')
