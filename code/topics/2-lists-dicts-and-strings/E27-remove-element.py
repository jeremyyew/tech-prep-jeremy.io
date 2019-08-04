'''
- We are only removing a single, given value so we only need one-pass to identify duplicates. Otherwise we would have to consider sorting to avoid O(N^2).
- **If we `del` or `remove` on sight, we have overall O(N^2)/O(KN) due to shifting.**
- **Instead, we overwrite from the end and pop it off in O(1), since no shifting.**
- Instead of checking if the last element is actually O(1) first (and perhaps shifting leftward till it is), we simply commit to checking the new value the next loop (no increment of i). 
'''

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while nums and i < len(nums):
            if nums[i] == val:
                nums[i] = nums[-1]
                nums.pop()
            else: 
                i += 1
        return len(nums)