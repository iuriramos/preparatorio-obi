N = int(input())
D = int(input())
A = int(input())

if A <= D:
    # aeronave acima do disco voador
    print(D-A)
else:
    # aeronave abaixo do disco voador
    print(N-(A-D))
