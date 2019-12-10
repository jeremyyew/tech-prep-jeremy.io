from collections import defaultdict
from typing import List


class Solution:
    def subarraySumTwoPass(self, nums: List[int], k: int) -> int:
        curr = 0
        res = 0
        partial_sums = []
        for n in nums:
            curr += n
            partial_sums.append(curr)
        seen = defaultdict(int)
        # Base case, j == k.
        seen[0] = 1
        for j in partial_sums:
            print(j-k, j, seen[j-k])
            res += seen[j-k]
            seen[j] += 1
        return res

    def subarraySum(self, nums: List[int], k: int) -> int:
        # One pass.
        curr, res, partial_sums = 0, 0, []
        seen = defaultdict(int)
        # Base case, j == k.
        seen[0] = 1
        for n in nums:
            curr += n
            res += seen[curr-k]
            seen[curr] += 1
        return res


r = Solution().subarraySum([1, 1, 1], 2)
assert(r == 2)


r = Solution().subarraySum([1, 2, 2, 3, 2, 3, 2, 2, 1], 5)
assert(r == 6)
