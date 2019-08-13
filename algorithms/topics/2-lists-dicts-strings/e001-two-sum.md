# E1-two-sum

* One-pass with dict: O\(N\) time, O\(N\) space. 
* Can we do it without dict but still better than O\(N^2\)?
* Two-pointers: O\(NlogN\) time, O\(N\) space.
* Can we do two-pointers in less than O\(N\) space? 
  * Since we are requesting for the index and not value, we have to store the original indexes either before sorting, or with individual elements, which is still O\(N\) space. 
  * Assume sort in place. 
  * Perhaps we could traverse the original array in one pass to find the original indexes of that pair. But that means saving the original array.
  * Only if output is value and not index then we can do it in O\(1\) space. 

```python
class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in seen:
                return [i, seen[complement]]
            seen[n] = i


class SolutionTwoPointers:
    def twoSum(self, nums, target):
        nums = list(enumerate(nums))
        nums.sort(key=lambda e: e[1])
        l, r = 0, len(nums) - 1
        while l < r:
            # print(l, r, nums)
            two_sum = nums[l][1] + nums[r][1]
            if two_sum < target:
                l += 1
            elif two_sum > target:
                r -= 1
            else:
                return [nums[l][0], nums[r][0]]
        return None


# r = SolutionTwoPointers().twoSum([3, 2, 4], 6)
# print(r)

```



