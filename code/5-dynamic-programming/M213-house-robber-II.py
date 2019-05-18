'''
See https://leetcode.com/problems/house-robber-ii/discuss/59978/6-lines-function-body. 

Suppose we have `nums = [X_1, X_2...X_N-2, X_N-1, X_N]`, and suppose a solution for houses from index `x` to `N` in nums is defined to be `dp(nums[x:N])`.  

Then the solution is similar to E198-house-robber except that we have a special case at the end:

When `i = N`: (on last house)
    `dp(nums[0:N]) = max(nums[N] + dp(nums[1:N-2]), dp(0:N-1))`

Basically, `nums[N] + dp(nums[1:N-2]) = nums[1:N]`, and this is saying "compare `nums[1:N]` and `nums[0:N-1]`".  
One way to obtain `nums[1:N]` is to "remove `X_1` from `nums[0:N]` if `X_1` was selected to be robbed".  
But there's no obvious way to keep track of whether `X_1` was selected. So another way to do so is to simply run the same solution for `nums[1:N]`.  
We need the base case `N = 1`, because both `nums[1:]` and `nums[:-1]` exclude `nums[0]`. 
'''


class Solution:
    def rob(self, nums):
        def rob_row(nums):
            now = prev = 0
            for n in nums:
                now, prev = max(now, prev + n), now
            return now
        if len(nums) == 1:
            return nums[0]
        return max(rob_row(nums[1:]), rob_row(nums[:-1]))
