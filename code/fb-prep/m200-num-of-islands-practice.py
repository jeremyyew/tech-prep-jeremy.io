class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        I, J = len(grid), len(grid[0])
        count = 0

        def dfs(i, j):
            if grid[i][j] == '1':
                grid[i][j] = '0'
                nbs = ((i, j) for i, j in
                       ((i+1, j), (i, j+1), (i-1, j), (i, j-1))
                       if 0 <= i < I and 0 <= j < J)
                for x, y in nbs:
                    dfs(x, y)

        for i in range(I):
            for j in range(J):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count
