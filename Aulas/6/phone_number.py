keyboard = ['', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

def helper(string, index):
    # caso base
    if index == len(string):
        return ['']
    # recursão
    num = string[index] # 1, 2, 3, 4
    combinacoes = helper(string, index + 1)
    resultado = []
    for combinacao in combinacoes:
       letras = keyboard[int(num)]
       for letra in letras:
            resultado.append(letra + combinacao)
    return resultado
     

def phone_number(string):
    if string == '':
        return []
    return helper(string, 0) # 1234
    
print(phone_number('1234'))
