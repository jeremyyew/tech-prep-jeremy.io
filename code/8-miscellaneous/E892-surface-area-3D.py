import unittest

class TestSurfaceArea(unittest.TestCase):
    def test_SurfaceArea(self):
        self.assertEqual(Solution().surfaceArea([[1,1,1],[1,0,1],[1,1,1]]), 32)
        self.assertEqual(Solution().surfaceArea([[2,2,2],[2,1,2],[2,2,2]]), 46)

 
class Solution:
    def surfaceArea(self, grid: 'List[List[int]]') -> 'int':
        N = len(grid)
        SINGLE_SURFACE = 1
        total_area = 0
        for i in range(N):
            for j in range(N):
                v = grid[i][j]
                cell_area = 0
                if v > 0: 
                    # Top and bottom. 
                    cell_area += SINGLE_SURFACE * 2

                left, right, up, down = 0, 0, 0, 0
                if j > 0: 
                    left = grid[i][j - 1]
                if j < N - 1:
                    right = grid[i][j + 1]
                if i > 0:
                    up = grid[i - 1][j]
                if i < N - 1:
                    down = grid[i + 1][j]
                for adjacent in [left, right, up, down]:
                    for cube in range(v): 
                        # print("adjacent", adjacent)
                        if adjacent < cube + 1:
                            cell_area += 1
                # print(cell_area)
                total_area += cell_area
        return total_area                                
unittest.main()