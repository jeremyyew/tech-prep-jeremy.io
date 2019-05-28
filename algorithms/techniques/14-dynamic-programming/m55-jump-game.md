# M55-jump-game

{% hint style="info" %}
Keep track of the minimal \(leftmost\) 'edge' that we must be able to jump to, such that we can eventually jump to`N`. If we can jump to an edge from `i`, `i` becomes our new edge.
{% endhint %}

Solution 2 makes the most sense and is the most performant, so it's the main one.

1. **Iterative, backwards, O\(N\) space:**

   Let `dp[i]` be a boolean value for whether we can jump from `i` to the last index `N`. Let `edges[i]` be the leftmost \(smallest\) index so far from `i` to `N` such that if we can jump to `edges[i]` \(NOT `i`\), we can eventually jump to `N`.

   * Base case: `dp[N] = True`, `edges[N] = N`
   * if `i + nums[i] >= edges[i]:`
     * we can jump to `edge` from `i`.
     * `edges[i] = i`
     * `dp[i] = True`
   * else:
     * we can't jump to `edge` from `i`, so the edge remains the same.
     * `edges[i] = edges[i+1]`

       `dp[i] = False`

2. **Iterative, backwards, O\(1\) space:**
   * Furthermore, we actually only need the previous `edge` to compute the next `edge`, and we don't need any intermediate `dp` values, so we shouldn't have to save all the previous `dp` or `edge` values.
3. **Recursive:**
   * We need to find successive `edges`, we don't actually need to find `dp[i]` till the end. So, the key recurrence relation can just be about `edges`.
   * Recurrence: `edges(i) = i if i + nums[i] >= edges(i+1) else edges[i+1]`
   * It runs quickly enough if you make sure to only make one recursive call - it's O\(N\), no repeated calls so no need memoization. 

```python
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        i_to_edge = True
        edge = N-1
        for i in range(N-2, -1, -1):
            if i + nums[i] >= edge:
                edge = i
                i_to_edge = True
            else:
                i_to_edge = False
        return i_to_edge


class SolutionIterativeBackwardsMemo:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        dp = [False for _ in range(N)]
        edges = [False for _ in range(N)]
        dp[N-1] = True
        edges[N-1] = N-1
        for i in range(N-2, -1, -1):
            if i + nums[i] >= edges[i+1]:
                edges[i] = i
                dp[i] = True
            else:
                edges[i] = edges[i+1]
        return dp[0]


class SolutionRec:
    def canJump(self, nums: List[int]) -> bool:
        def edges(i: int) -> int:
            if i == len(nums)-1:
                return i
            edges_next = edges(i+1)
            return i if i + nums[i] >= edges_next else edges_next
        return edges(0) == 0

```

