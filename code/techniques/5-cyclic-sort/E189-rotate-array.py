'''
- Challenge is to be in place, O(1) space. Otherwise just concatenate and reassign. 
- Can either reverse multiple times, or cyclic replace (must write your own in-place reverse, for some reason Python's reverse is supposed to be in-place but doesn't work). 
'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, temp = 0, nums[0]
        while True: 
            j = (i + k) % len(nums)
            v = temp 
            temp = nums[j] 
            nums[j] = v
            i = j
            if i == 0: 
                break

        