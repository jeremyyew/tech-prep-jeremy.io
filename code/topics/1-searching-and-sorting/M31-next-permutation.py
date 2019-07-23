import math

class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        inv = None
        for i in reversed(range(len(nums) - 1)):
            if nums[i] < nums[i + 1]:
                inv = i
                break
        if inv is None:
            nums.sort()
            return
        next_biggest, k = math.inf, None
        for i in range(inv+1, len(nums)):
            if nums[i] > nums[inv] and nums[i] < next_biggest:
                next_biggest = nums[i]
                k = i
        if k is not None:
            nums[k] = nums[inv]
            nums[inv] = next_biggest 
        nums[inv+1:] = sorted(nums[inv+1:])
        return

l = [5,1,1]
Solution().nextPermutation(l)
print(l)