# M62-unique-paths

_A robot is located at the top-left corner of a m x n grid \(marked 'Start' in the diagram below\)._

_The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid \(marked 'Finish' in the diagram below\)._

_How many possible unique paths are there?_

\_\_![](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)  
_Above is a 7 x 3 grid. How many possible unique paths are there?_

_**Note:** m and n will be at most 100._

_**Example 1:**_

```text
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
```

{% hint style="info" %}
Observe that to get to some cell `(i, j)`, we can only travel from two adjacent cells `(i-1, j)` or `(i, j-1)`. Hence, the number of ways to get to cell `(i,j)` is the number of ways to get to `(i-1, j)` plus the number of ways to get to `(i, j-1)`.
{% endhint %}

Formally, 

\[1\] **`dp(i, j) = dp(i-1, j) + dp(i, j-1)`.**

See `Solution` for `M` variables, and `SolutionGridMemo` for `MxN` variables.

Further notes:

\[2\] We can set the `0`th rows to `0` so that we only need to declare one base case `(1,1)` and all the other base cases will also arise from the recurrence.

\[3\] Furthermore to compute the next row, instead of the entire grid for we really only need the previous `row` and the left cell `l`.

\[4\] Remember, if we do \[3\], we need to reset `l=0` on every row, and also write the current value to `row[j]` on every column.

\[5\] Also remember not to use multiplication operator if we're making a grid, you'll get references.

```python
class Solution:  # [3]
    def uniquePaths(self, m: int, n: int) -> int:
        row = [0 for _ in range(n + 1)]  # [2]
        for i in range(1, m+1):
            l = 0  # [4]
            for j in range(1, n+1):
                if i == 1 and j == 1:
                    row[j] = l = 1  # [2], [4]
                else:
                    row[j] = l = row[j] + l  # [1], [4]
        return row[n]


class SolutionGridMemo:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]  # [2], [5]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == 1 and j == 1:
                    dp[i][j] = 1  # [2]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]  # [1]
        return dp[m][n]

```

