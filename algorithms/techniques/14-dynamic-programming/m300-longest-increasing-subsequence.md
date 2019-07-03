# M300-longest-increasing-subsequence

**Solution DP: O\(N^2\) time, O\(N\) space.**

* For each subseqence ending in the i-th element, we obtain its max length by finding the max length of all previous subsequences that end in some j-th element nums\[j\] that is less than nums\[i\] \(where j &lt; i\), and then we add one. 
* Recurrence relation: 
  * `lengths[i] = max{lengths[j] where 0 < j < i and nums[j] < nums[i]} + 1`
* We could then compare lengths\[i\] with the max length so far to see if it is the new longest subsequence length. However in this implementation, we only find the max at the end since we don't really need it intermediately. s
* Even if lengths\[i\] isn't a new max, we still need to save it, since it may end up being part of a new max later on. 

**Solution Binary Search \(submitted\): O\(NlogN\) time, O\(N\) space.**

* See solution. 
* Initialize with infinity so that bisect will point towards the left \(generally you can do this whenever you want binary search on a variable length\).
* Keep track of length. 
* Python's bisect always returns the insertion point. 
* See M334 as well, this is kind of a generalization.

```python
from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        inc = [float('inf')] * 2
        l = 0
        for num in nums:
            # i is insertion point
            i = bisect.bisect_left(inc, num) 
            if i == l: 
                l += 1 
            inc[i] = num
        return l


class SolutionDP:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        lengths = [None for _ in range(len(nums))]
        lengths[0] = 1
        for i in range(1, len(nums)):
            lengths[i] = 1 + max(
                [lengths[j]
                 for j in range(i)
                 if nums[j] < nums[i]] or [0])
        return max(lengths)

```

