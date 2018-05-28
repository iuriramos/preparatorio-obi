N = int(input()) # 2
linhas = [] # {}, }{

while N > 0: #
    linha = input() # }{
    linhas.append(linha) # {}, }{
    N -= 1 # N = 0
# join >> lista >> str
# split >> str >> lista
string = ''.join(linhas)
diff = 0
for ch in string:
    if ch == '{':
        diff += 1
    elif ch == '}':
        diff -= 1
    if diff < 0:
        break     
if diff == 0:
    print('S')
else:
    print('N')

