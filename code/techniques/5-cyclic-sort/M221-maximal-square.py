class Solution:
    def maximalSquare(self, A):
        if len(A) == 0:
            return 0
        for i in range(len(A)):
            for j in range(len(A[i])):
                A[i][j] = int(A[i][j])
                if A[i][j] and i > 0 and j > 0:
                    A[i][j] = min(A[i-1][j],
                                  A[i-1][j-1],
                                  A[i][j-1]) + 1
        return max(map(max, A)) ** 2
