# M200-number-of-islands

[https://leetcode.com/problems/number-of-islands](https://leetcode.com/problems/number-of-islands)

_Given a 2d grid map of '1's \(land\) and '0's \(water\), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water._

* Iterate through all nodes. 
* For each node, **do DFS to traverse all connected nodes and mark all as visited.** Count as one island. 
* When visiting these visited nodes later we will simply skip them. 
* Thus time complexity O\(N\).

```python

class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        I, J = len(grid), len(grid[0])

        def dfs(i, j):
            if not (0 <= i < I and
                    0 <= j < J):
                return
            if (grid[i][j] == '1'):
                grid[i][j] = '0'
                for x, y in ((i+1, j), (i-1, j),
                             (i, j+1), (i, j-1)):
                    dfs(x, y)

        count = 0
        for i in range(I):
            for j in range(J):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count

```

