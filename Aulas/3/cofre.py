N, M = [int(s) for s in input().split()]
nums = [int(s) for s in input().split()]
seq  = [int(s)-1 for s in input().split()]

def cofre(nums, seq):
    if not seq:
        return [0] * 10
    entrada = []
    saida = []
    # for (int i = 0; i < M - 1; i++) {
    #    int curr = seq[i];
    #    int next = seq[i + 1];
    #   
    for i in range(len(seq) -1):
        curr = seq[i]
        next = seq[i + 1]
        if i > 0:
            if curr < next:
                curr += 1
            else:
                curr -= 1
        if curr > next:
            curr, next = next, curr
        entrada.append(curr)
        saida.append(next)
    
    entrada.sort()
    saida.sort()
    # print(entrada, saida)
    
    segredo = [0] * 10
    i, j = 0, 0
    count = 0
    for k in range(len(nums)):
        if i < len(entrada) and k == entrada[i]:
            count += 1
            i += 1
        num = nums[k]
        segredo[num] += count
        if j < len(saida) and k == saida[j]:
            count -= 1
            j += 1
    return segredo
    
segredo = cofre(nums, seq)
for s in segredo:
    print (s, end=' ')
