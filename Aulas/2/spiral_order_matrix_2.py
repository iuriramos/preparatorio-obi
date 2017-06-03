# Spiral Matrix

def spiral_matrix_2(matrix):
    N, M = len(matrix), len(matrix[0])
    top, down = 0, N -1
    left, right = 0, M -1
    k = 1
    i, j = 0, 0
    while k <= N*M:
        print(matrix[i][j])
        if i == top:
           j += 1
           if j > right:
            i += 1
            j -= 1
        elif j == right:
           i += 1
           if i > down:
               j -= 1
               i -= 1
        elif i == down:
           j -= 1
           if j < left:
               i -= 1
               j += 1
        elif j == left:
           i -= 1
           if i == top:
               i += 1
               j += 1
               left += 1
               right -= 1
               top += 1
               down -= 1
        k += 1
 
if __name__ == '__main__':
    # entrada: 
    # linha 1: N M
    # linha 2: < N * M números > para montar a matriz N * M
    N, M = [int(s) for s in input().split()]
    numbers = [int(s) for s in input().split()]
    matrix = [[0] * M for _ in range(N)] # matrix N * M
    # populate matrix
    k = 0 # index for numbers
    for i in range(N):
        for j in range(M):
            matrix[i][j] = numbers[k]
            k += 1 
    spiral_matrix_2(matrix)
   
        
