# E377-combination-sum-IV

_Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target._

**Example:**

```text
nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
```

_**Follow up:**  
What if negative numbers are allowed in the given array?  
How does it change the problem?  
What limitation we need to add to the question to allow negative numbers?_

We can obtain the number of combinations that form a target i by checking how many combinations form each sub-target k, where k + n = i and n is a number we add to combinations of k to form i.

More formally: `dp[i] = sum{dp[i-n] where i > n, and if i == n then 1}`

Time complexity: `O(target * |nums|)`.

```python
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if target < 1:
            return 0
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for n in nums:
                dp[i] += dp[i-n] if i >= n else 0
        return dp[target]
```

