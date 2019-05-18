# E46-permutations

```python
from typing import List

# note assume no dups 

class SolutionRec:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1: 
            return [nums]
        perms = []   
        for i in range(0, len(nums)):
            first = nums[i] # pick every character to be the first
            sub_nums = nums[0:i] + nums[i+1:] # get all other characters
            sub_perms = self.permute(sub_nums)
            for perm in sub_perms: 
                perms.append([first] + perm) 
        return perms
# in iterative version, instead of forming new lists, we can keep track of the indexes of the elements to be left out in the original lists
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]] 
        for n in nums: 
            new_perms = []
            for perm in perms:
                for i in range(0, len(perm) + 1):
                    new_perms.append(perm[:i] + [n] + perm[i:])
            perms = new_perms
        return perms
```

