"""
Dada a matriz:
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Retorne-a em ordem espiral: [1, 2, 3, 6, 9, 8, 7, 4, 5]
"""

class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        result = []
        start_i, end_i = 0, len(A) - 1
        start_j, end_j = 0, len(A[0]) - 1
        i, j, n = start_i, start_j, len(A) * len(A[0])
        for _ in range(n):
            result.append(A[i][j])
            if i == start_i and j != end_j:
                j += 1
            elif j == end_j and i != end_i:
                i += 1
            elif i == end_i and j != start_j:
                j -= 1
            elif j == start_j and i != start_i:
                i -= 1
                if i == start_i:
                    start_i += 1
                    end_i -= 1
                    start_j += 1
                    end_j -= 1
                    i, j = start_i, start_j
        return result

if __name__ == '__main__':
    s = Solution()
    result = s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(result)
