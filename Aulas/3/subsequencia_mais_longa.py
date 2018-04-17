# problema de interpretação, mais simples do que parece...
s = input()
t = input()

if len(s) >= len(t):
    return len(s)
else: # len(t) > len(s)
    return len(t)    
