'''
We can't do two-pointers because:

the values are not sorted. So shifting left or right will not guarantee an increase or decrease in the current sum.

we aren't trying to quantify on the length of the subarray(e.g. min length or max-length)

We can't do sliding-window because:

the values may be positive or negative. So adding one or removing one element will not guarantee and increase or decrease in the current sum.

Generate an array of partial sums. The difference between any two partial sums i and j is the sum contained in the elements from i to j. So we simply have to run a two-sum algorithm on this array of partial sums to find all that add to the target k.

Procedurally, we can do a one-pass, keeping a counter of how many of each sums we have seen(since the current partial sum could form k with multiple other previous indices.)
'''

from typing import List
import collections


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = collections.Counter()
        total = 0
        res = 0
        for i, n in enumerate(nums):
            total += n
            res += sums[total - k]
            sums[total] += 1
            if total == k:
                res += 1
        return res


​
