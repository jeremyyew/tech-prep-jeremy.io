# E70-climbing-stairs

_You are climbing a stair case. It takes n steps to reach to the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top? **Note:** Given n will be a positive integer._

* Base cases:
  * `n = 1`, so `1`.
  * `n = 2`, so `1+1` or `2`.
* Inductive case:
  * `dp(n) = dp(n-1) + dp(n-2)`

Here we present all 4 DP versions: 

1. Recursive \(top down\) - TLE.  
2. Recursive \(top down\) w Memo.  
3. Iterative \(bottom up\) w O\(N\) memory.  
4. Iterative \(bottom up\) w O\(1\) memory.

```python
import functools
class Solution1:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)


class Solution2:
    @functools.lru_cache()
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)


class Solution3:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [None] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prev2, prev1 = 2, 1
        for _ in range(3, n + 1):
            prev2, prev1 = prev2 + prev1, prev2
        return prev2

```

