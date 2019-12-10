import heapq
import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distances = [(math.sqrt(x**2 + y**2), [x, y]) for x, y in points]
        heapq.heapify(distances)
        res = []
        for _ in range(K):
            _, coord = heapq.heappop(distances)
            res.append(coord)
        return res


r = Solution().kClosest([[1, 3], [-2, 2]], 1)
print(r)
assert(r == [[-2, 2]])

r = Solution().kClosest([[3, 3], [5, -1], [-2, 4]], 2)
print(r)
assert(r == [[3, 3], [-2, 4]])
