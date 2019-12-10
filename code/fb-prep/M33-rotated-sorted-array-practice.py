'''
The unexpectedly simple trick to make binary search work despite the rotation: essentially, using an offset to get the true midpoint - otherwise the binary search is exactly the same! 

[1] We project from the current midpoint index to get the 'real' midpoint value (via a modulus shift of the rotation places), which we then compare with the target. 

[2] Consequently, moving l and r as per normal binary search will also shift the realMid along the ordered array. 

- For example, if nums[realMid] < target, we move l to the mid. Yes we might have left the target outside of nums[l:r]; however, we are trying to zero in on the target using our offset realMid, not mid directly, so that's ok. Thus we are actually shifting realMid to make our next guess to the right by (m-l)//2 places.   

[3] Of course, we also have to obtain the rotation point; see M153-find-minimum-in-rotated-sorted-array for explanation. 

[4] Also remember to make findMin return index not value!

Adapted from https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14425/Concise-O(log-N)-Binary-search-solution. 
'''
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return None
        offset = self.findMin(nums)
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            real_mid = (m + offset) % len(nums)
            if nums[real_mid] == target:
                return real_mid
            elif nums[real_mid] < target:
                l = m + 1
            else:
                r = m - 1
        return -1

    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if nums[l] < nums[r]:
            return l
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return l


6, 7, 0, 1, 2, 3, 4, 5

r = Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=0)
print(r)
assert(r == 4)


r = Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=3)
print(r)
assert(r == -1)
