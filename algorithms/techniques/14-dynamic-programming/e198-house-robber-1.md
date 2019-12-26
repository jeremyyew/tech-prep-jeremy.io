# E198-house-robber

_You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**._

_Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight **without alerting the police**._

{% hint style="info" %}
We rob house `i` if doing so is a bigger increase from `i-2` than sticking with`i-1`. 
{% endhint %}

* The max value of robbing houses from house `0` to `i`, `dp(i)`, depends on whether to rob house `i`. 
* If we rob house `i`, we should rob as much as we can from every house except house `i-1`. It doesn't matter which combination of houses we rob, as long as we avoid house `i-1`; this is given by `dp(i-2)`. 
  * If `dp(i-2)` actually happens to leave out `i-2`, that's fine because that means it still gives a larger value than including `i-2`, so we still get the maximum out of houses `0`to `i-2`.
  * In the case where `dp(i-1)` doesn't actually include `i-1` either, then we should definitely rob house `i`, and this will happen since `dp(i-2) == dp(i-1)`.
* So, we rob house `i` if `nums[i] + dp(i-2) > dp(i-1)`. 

Formally, 

```text
dp(i) = max(nums[i] + dp(i-2), dp(i-1)). 
```

Below is 'level 4' solution, iterative + N variables.

The other one, `SolutionIterativeMemo` is level 3 and relatively more readable.

See [https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems](https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems).

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 0:
            return 0
        prev1, prev2 = 0, 0
        for i in range(N):
            prev1, prev2 = max(nums[i] + prev2, prev1), prev1
        return prev1


class SolutionIterativeMemo:
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

