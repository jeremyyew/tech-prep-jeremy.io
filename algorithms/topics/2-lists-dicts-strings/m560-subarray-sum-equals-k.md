# M560-subarray-sum-equals-k

* We can't do two-pointers because: 
  * the values are not sorted. So shifting left or right will not guarantee an increase or decrease in the current sum.
  * we aren't trying to quantify on the length of the subarray \(e.g. min length or max-length\)
* We can't do sliding-window because:
  * the values may be positive or negative. So adding one or removing one element will not guarantee and increase or decrease in the current sum. 
* Generate an array of partial sums. The difference between any two partial sums `i` and `j` is the sum contained in the elements from `i` to `j`. So we simply have to run a two-sum algorithm on this array of partial sums to find all that add to the target `k`. 
* Procedurally, we can do a one-pass, keeping a counter of how many of each sums we have seen \(since the current partial sum could form `k` with multiple other previous indices.\)

```python
from collections import Counter


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Base case: when the current sum is equal to the target, we will add sum_counts[0] = 1.
        sum_counts = Counter([0])
        res, curr_sum = 0, 0
        for n in nums:
            curr_sum += n
            comp_sum = curr_sum - k
            if comp_sum in sum_counts:
                res += sum_counts[comp_sum]
            sum_counts[curr_sum] += 1
        return res
```

