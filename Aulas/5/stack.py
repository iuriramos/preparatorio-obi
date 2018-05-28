# (([{}{}()[]])(){}){}
# {['}]
# pilha = [{, [, ]
# ([ ')] >> pilha = [(, [, 
# ]
N = int(input())
while N > 0:
    linha = input()
    pilha = []
    valido = True
    for ch in linha:
        #if ch == '(' or ch == '[' or ch == '{':
        if ch in '([{':
            pilha.append(ch)
        else: # ch == ] or ch == )
            if not pilha: # pilha == []
                valido = False
                break
            elif ch == ']' and pilha[-1] == '[':
                pilha.pop()
            elif ch == ')' and pilha[-1] == '(':
                pilha.pop()
            elif ch == '}' and pilha[-1] == '{':
                pilha.pop()
            else:
                valido = False
                break
    # end for loop
    if valido:
        if not pilha: # pilha == []:
            print ('S')
        else:
            print ('N')
    else:
        print('N')
    # decrementar contador
    N -= 1
    
