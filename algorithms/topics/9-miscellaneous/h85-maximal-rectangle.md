# H85-maximal-rectangle

_Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area._

_**Example:**_

```text
Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
```

* [https://leetcode.com/problems/maximal-rectangle/discuss/29136/Python-solution-using-maximum-histogram](https://leetcode.com/problems/maximal-rectangle/discuss/29136/Python-solution-using-maximum-histogram)

First calculate the height for each row. Then convert this problem to finding the largest rectangle in histogram by computing the rectangle row by row and take the maximum.

```python
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0: return 0
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[i])):
                if i == 0: 
                    matrix[i][j] = int(matrix[i][j])
                    continue
                if matrix[i][j] == '1':
                    matrix[i][j] = matrix[i-1][j] + int(matrix[i][j])
                else:
                    matrix[i][j] = 0
        return max([self.maxRectangle(row) for row in matrix])
        
    def maxRectangle(self, hist):
        stk = []
        maxx = 0
        hist.append(0)
        for i in xrange(len(hist)):
            while len(stk) > 0 and hist[i] < hist[stk[-1]]:
                s = stk.pop()
                if len(stk) == 0:
                    maxx = max(maxx, i*hist[s])
                else:
                    maxx = max(maxx, (i - stk[-1] - 1)*hist[s])
            stk.append(i)
        return maxx
```

