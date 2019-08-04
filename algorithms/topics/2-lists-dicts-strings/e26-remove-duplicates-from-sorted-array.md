# E26-remove-duplicates-from-sorted-array

* It's sorted so we only need one-pass to identify duplicates. 
* If we `del` or `remove` on sight, we have overall O\(N^2\)/O\(KN\) due to shifting. 
* Instead, we accumulate a list of unique values from the left. 
* We only add a new distinct value when we just see it; afterwards, we ignore its duplicates and wait till we see the next distinct element. 

```python
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
```

