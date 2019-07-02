'''
- If zero, add to zeros, which is the number of consecutive zeroes directly before index i.
- If non-zero and we have no consecutive zeros: pass.
- If non-zero and we have at least one zero before i:
    - swap the first zero(at index i - zeros) with the current value.
    - note that the number of consecutive zeroes before i remains the same.
'''


class Solution(object):
    def moveZeroes(self, nums):
        i = 0
        zeros = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            elif zeros > 0:
                nums[i - zeros] = nums[i]
                nums[i] = 0

        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
