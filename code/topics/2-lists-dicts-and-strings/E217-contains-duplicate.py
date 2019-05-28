from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for e in nums:
            if e in seen:
                return True
            seen[e] = True
        return False
        