# 11. Modified Binary Search \(1E, 0M\)

1. Simply set a flag to False, that will be replaced with the target if found. 
2. Remember to avoid integer overflow when getting midpoint. 

```python
class Solution(object):
    def search(self, nums, target):
        t = -1  # [1]
        l, r = 0, len(nums) - 1  # [2]
        while l <= r:
            m = l + ((r-l) // 2)
            if target == nums[m]:
                t = m
                break
            elif target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        return t

```

