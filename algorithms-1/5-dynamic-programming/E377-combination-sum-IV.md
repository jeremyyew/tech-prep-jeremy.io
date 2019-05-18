# E674-longest-continuous-increasing-subarray

```python
'''
DP, iterative and linear.
Let OPT_WITH(i) be the maximum length of a continuous increasing sequence that ends in nums[i].
Let OPT(i) be the maximum length of all continuous increasing sequences in nums from 0 to i.

To compute the next OPT_WITH(i), we need OPT_WITH(i-1) to decide whether we can extend the current increasing sequence with nums[i], or start over from nums[i].
    - If nums[i-1] < nums[i], it is still an increasing sequence so we can append nums[i] and increase the length by 1. This will always be better than not appending.
    - If nums[i-1] >= nums[i], we can't append nums[i], so we have to start from nums[i] and set OPT_WITH(i) to 0.

To compute the next OPT(i), we need OPT(i-1) and OPT_WITH(i) to decide whether we have found a new max, or keep the current max.

More formally:
    OPT_WITH(i) = if nums[i-1] < nums[i]
                  then OPT_WITH(i-1) + 1
                  else 1

    OPT(i) = max(OPT(i-1), OPT_WITH(i))
'''


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 1:
            return N
        OPT_WITH = OPT = 1
        for i in range(1, N):
            OPT_WITH = OPT_WITH + 1 if nums[i-1] < nums[i] else 1
            OPT = max(OPT, OPT_WITH)
        return OPT

```

