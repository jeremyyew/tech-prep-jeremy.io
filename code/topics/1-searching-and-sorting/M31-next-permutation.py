'''
- The next permutation is the smallest number that is larger than the current number. 
- To obtain the next permutation, we must increase the smallest (rightmost) value that can be increased by swapping it with the smallest next value on its right (using a value on its left will have larger impact on the magnitude).
- Therefore, we swap the rightmost 'inversion' (small-big) with the minimum greater number on its right. 
- If there are no inversions, the permutation is already max value. 
- After swapping, we need to sort the segment on the right such that it is the minimum value possible, i.e. ascending order. Any non-minimum value will be a larger value than our candidate.
- Actually, we can simply reverse this segment since we have already established it is strictly decreasing. 
'''


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


# l = [1, 2, 3]
# Solution().nextPermutation(l)
# print(l)
