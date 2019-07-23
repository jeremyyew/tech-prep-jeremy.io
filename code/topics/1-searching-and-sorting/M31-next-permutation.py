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
        k = None
        for i in range(inv+1, len(nums)):
            if nums[i] > nums[inv] and (k is None or nums[i] < nums[k]):
                k = i
        if k is not None:
            temp = nums[k]
            nums[k] = nums[inv]
            nums[inv] = temp
        nums[inv+1:] = sorted(nums[inv+1:])
        return

l = [1,2,3]
Solution().nextPermutation(l)
print(l)