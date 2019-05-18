# M673-number-of-longest-increasing-subsequence

```python
'''

- See LIS for explanation of getting lengths. We use loops here instead of list comprehension as it is easier to express the setting/adding of counts. We also use 0 instead of None for initial values since we'll need to compare the initial value in lengths[i].

- In this solution we simply keep the list counts, and set to the number of subsequences of the prefix when we find a new max length, and add one when we see a subsequence of the same length again. 

lengths[i] = longest subsequence ending in nums[i]
counts[i] = number of longest subsequences ending in nums[i]

[1] For each subsequence ending in nums[j], if it is a new max value, add it to lengths[i] and set the number of longest subsequences ending in nums[i], i.e. counts[i], to counts[j] (the number of ways to construct the prefix is the number of ways to construct the new subsequence). 

[2] Else if it is an existing max value, add to counts[i].

Adapted from https://leetcode.com/problems/number-of-longest-increasing-subsequence/solution/
'''

from collections import Counter


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 1:
            return N
        lengths = [0 for _ in range(N)]
        counts = [1 for _ in range(N)]
        for i in range(N):
            for j in range(i):
                if nums[j] < nums[i]:
                    if lengths[j] + 1 > lengths[i]:  # [1]
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:  # [2]
                        counts[i] += counts[j]
        longest = max(lengths)
        return sum(c for i, c in enumerate(counts) if lengths[i] == longest)

```

