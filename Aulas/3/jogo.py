a, b, c ,d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)

time = (c*60 + d) - (a*60 + b)

if time > 0:
    x = time//60
    y = time%60
elif time == 0:
    x = 24
    y = 0
else: # time < 0
    time1 = 24*60 - time
    x = time1//60
    y = time1%60
    
print ('O jogo durou ' + str(x) + ' hora(s) e ' + str(y) + ' minuto(s).')
    
