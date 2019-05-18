# E377-combination-sum-IV

We can obtain the number of combinations that form a target i by checking how many combinations form each sub-target k, where k + n = i and n is a number we add to combinations of k to form i.  

More formally: 
    `dp[i] = sum{dp[i-n] where i > n, and if i == n then 1}`

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