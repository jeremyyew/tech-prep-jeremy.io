# H329-longest-increasing-path-in-a-matrix

* Memoize max path distance starting from every cell. Exactly like grid traversal DP, we must simply obtain all max paths. 
* Instead of re-traversing a cell that has already been computed, we lookup first in the memo. This keeps time to O\(N\), otherwise it could be O\(N^2\) or more. 
* We may only register and return the max path for the current cell once we have obtained the results from all its legal adjacent cells. 

```python
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        I, J = len(matrix), len(matrix[0])
        dp = [[None for _ in range(J)] for _ in range(I)]

        def neighbors(i, j):
            nbs = [(i-1, j), (i+1, j),
                   (i, j-1), (i, j+1)]
            return [(i, j) for (i, j) in nbs
                    if 0 <= i < I
                    and 0 <= j < J]

        def max_path_from(i, j):
            if dp[i][j]:
                return dp[i][j]
            increasing_nbs = [(x, y) for x, y in neighbors(i, j)
                              if matrix[x][y] > matrix[i][j]]
            res = max([max_path_from(x, y)
                       for x, y in increasing_nbs], default=0) + 1
            dp[i][j] = res
            return res

        path_lengths = [max_path_from(i, j)
                        for j in range(J) for i in range(I)]
        return max(path_lengths)


# r = Solution().longestIncreasingPath(
#     [
#         [3, 4, 5],
#         [3, 2, 6],
#         [2, 2, 1]
#     ])
# print(r)
# assert(r == 4)


# r = Solution().longestIncreasingPath(
#     [
#         [9, 9, 4],
#         [6, 6, 8],
#         [2, 1, 1]
#     ])
# print(r)
# assert(r == 4)


```

