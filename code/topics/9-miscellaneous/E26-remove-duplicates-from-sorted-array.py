class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = 0
        for n in nums[1:]:
            if n != nums[curr]: 
                curr += 1
                nums[curr] = n
        nums = nums[:curr+1]
        return len(nums)