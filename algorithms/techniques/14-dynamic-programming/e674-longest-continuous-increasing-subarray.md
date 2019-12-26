# E674-longest-continuous-increasing-subarray

_Given an unsorted array of integers, find the length of longest `continuous` increasing subsequence \(subarray\)._

DP, iterative and linear. Let OPT\_WITH\(i\) be the maximum length of a continuous increasing sequence that ends in nums\[i\]. Let OPT\(i\) be the maximum length of all continuous increasing sequences in nums from 0 to i.

To compute the next OPT\_WITH\(i\), we need OPT\_WITH\(i-1\) to decide whether we can extend the current increasing sequence with nums\[i\], or start over from nums\[i\].

* If nums\[i-1\] &lt; nums\[i\], it is still an increasing sequence so we can append nums\[i\] and increase the length by 1. This will always be better than not appending.
* If nums\[i-1\] &gt;= nums\[i\], we can't append nums\[i\], so we have to start from nums\[i\] and set OPT\_WITH\(i\) to 0.

To compute the next OPT\(i\), we need OPT\(i-1\) and OPT\_WITH\(i\) to decide whether we have found a new max, or keep the current max.

More formally: OPT\_WITH\(i\) = if nums\[i-1\] &lt; nums\[i\] then OPT\_WITH\(i-1\) + 1 else 1



```text
OPT(i) = max(OPT(i-1), OPT_WITH(i))
```

```python

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

