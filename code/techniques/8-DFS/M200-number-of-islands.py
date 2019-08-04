'''
- Iterate through all nodes. 
- For each node, do DFS to traverse all connected nodes and mark all as visited. Count as one island. 
- When visiting these visited nodes later we will simply skip them. 
- Thus time complexity O(N). 
'''


class Solution:
    def numIslands(self, grid) -> int:
        def dfs(i, j):
            if (grid[i][j] == '1' and
                0 <= i < len(grid) and
                    0 <= j < len(grid[i])):
                grid[i][j] = '0'
                map(dfs, ((i+1, j), (i-1, j),
                          (i, j+1), (i, j-1)))
        if not grid:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count
