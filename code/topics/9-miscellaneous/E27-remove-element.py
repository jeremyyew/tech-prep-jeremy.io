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