# H329-longest-increasing-path-in-a-matrix

* Memoize max path distance starting from every cell. Exactly like grid traversal DP, we must simply obtain all max paths. 
* Instead of re-traversing a cell that has already been computed, we lookup first in the memo. This keeps time to O\(N\), otherwise it could be O\(N^2\) or more. 
* We may only register and return the max path for the current cell once we have obtained the results from all its legal adjacent cells. 

```python
from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0:
            return 0
        nrows = len(matrix)
        ncols = len(matrix[0])
        maxLengths = [[None] * ncols for _ in range(nrows)]

        def legalSteps(x, y):
            steps = []
            curr = matrix[x][y]
            if x > 0 and matrix[x-1][y] > curr:
                steps.append((x-1, y))
            if x < nrows - 1 and matrix[x+1][y] > curr:
                steps.append((x+1, y))
            if y > 0 and matrix[x][y-1] > curr:
                steps.append((x, y-1))
            if y < ncols - 1 and matrix[x][y+1] > curr:
                steps.append((x, y+1))
            return steps

        def maxLengthFrom(x, y):
            if maxLengths[x][y]:
                return maxLengths[x][y]
            res = max([maxLengthFrom(p, q)
                       for p, q in legalSteps(x, y)] + [0]) + 1
            maxLengths[x][y] = res
            return res

        lengths = []
        for x in range(nrows):
            for y in range(ncols):
                lengths.append(maxLengthFrom(x, y))
        return max(lengths)


# r = Solution().longestIncreasingPath(
#     [
#         [3, 4, 5],
#         [3, 2, 6],
#         [2, 2, 1]
#     ])
# print(r)

```

