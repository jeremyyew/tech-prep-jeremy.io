# E198-house-robber

* The max value of robbing houses from house 0 to i, dp\(i\), depends on whether to rob house i. 
* If we rob house i, we should rob as much as we can except house i-1. It doesn't matter which combination of houses we rob, as long as we avoid house i-1; this is given by dp\(i-2\). 
* If dp\(i-2\) leaves out i-2 that's fine too because it still gives a larger value than including it. 
* In the case where dp\(i-1\) doesn't actually include i-1 either, then dp\(i-1\) = dp\(i-2\) and our condition passes, so we know we definitely should rob nums\[i\]. 
* **So, we rob house i if doing so is a bigger increase from i-2 than i-1 \(in a way, i-2 decides between i-1 and i\).**

Formally,

$$
\textrm{dp(i)} = \textrm{max}(\textrm{nums}[i] + \textrm{dp}(i-2),\textrm{dp}(i-1))
$$



```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 1:
            return N
        dp = [None] * (N+1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2, N + 1):
            dp[i] = max(nums[i-1] + dp[i-2], dp[i-1])
        return dp[N]

```

