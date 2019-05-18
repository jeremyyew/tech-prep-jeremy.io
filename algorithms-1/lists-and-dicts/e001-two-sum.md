# E1-two-sum

```python
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # collect complements x' in dict, with x' : index x
        # if next number y is a complement in dict, return indices of x, y 
        # one-pass
        comps = {}
        for i in range(len(nums)):
            x = nums[i]
            if x in comps: 
                return [comps[x], i]
            comps[target - x] = i

```



