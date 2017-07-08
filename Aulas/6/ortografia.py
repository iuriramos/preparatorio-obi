
def distance(dict_word, word, i, j, cache):
    # i - dict_word
    # j - word
    
    # caso base
    if i == len(dict_word):
        return len(word) - j # remove chars de word
    if j == len(word):
        return len(dict_word) - i # adiciona chars em word
          
    if cache[i][j] != -1:
        return cache[i][j]
        
    # recursão
    if dict_word[i] == word[j]:
        return distance(dict_word, word, i + 1, j + 1, cache)
    # adição
    min_ = distance(dict_word, word, i + 1, j, cache) + 1
    # remoção
    remocao = distance(dict_word, word, i, j + 1, cache) + 1
    min_ = min(remocao, min_)
    # troca
    troca = distance(dict_word, word, i + 1, j + 1, cache) + 1
    min_ = min(troca, min_)
    
    cache[i][j] = min_
    return min_
    

def ortografia(dictionary, words):
    line = []
    for word in words:
        for dict_word in dictionary:
            if abs(len(dict_word) - len(word)) > 2:
                continue
            cache = [[-1 for _ in range(20)] for __ in range(20)]
            d = distance(dict_word, word, 0, 0, cache)
            if d <= 2:
                line.append(dict_word)
        print (' '.join(line))
         
ortografia(['pato', 'pateta', 'caneca'], ['pata'])
