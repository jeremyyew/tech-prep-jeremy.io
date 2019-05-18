from typing import List
'''
Binary search. We compare the midpoint with the rightmost element of the current subarray to see if the rotation is on the left or right of the midpoint, until our left and right pointers converge. 

[1] Start with l, m, r indices.
[2] We loop till l == r.

Let L = nums[l:m] and R = nums[m+1:r]
[3] If nums[m] > nums[r], min is in R.
[4] Else nums[m] < nums[r], min is in L.

[5] Base case 0: if nums is empty, return None. 
[6] Base case 1: if nums is single element, we do not run the loop. 
[7] Base case 2: when l and r are consecutive, either could be min. l becomes m, and then rules from [3] and [4] help us select one.  
[8] Remember to check if there was any rotation at all by comparing l and r.


Proof of [3]: Suppose min is in L, then the rotation point is in L. But obviously we already seen a decrease in value, so the rotation point must be in R.
Proof of [4]: Suppose min is in R, then the rotation point is in R. But then since all values from the min onward used to be somewhere in front of nums[m], nums[r] should be less than nums[m] - a contradiction.


Adapted from https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14425/Concise-O(log-N)-Binary-search-solution. 
'''


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1  # [1]

        if len(nums) == 0:
            return None

        if nums[r] > nums[l]:  # [8]
            return nums[0]

        while l < r:  # [2], [6], [7]
            m = (l + r) // 2
            if nums[m] > nums[r]:  # [3]
                l = m + 1
            else:
                r = m  # [4]
        return nums[l]
