# E448-find-all-numbers-disappeared-in-an-array

1. **Cyclic Sort**: O\(N\) time, O\(1\) space. \(Submitted\)
2. **Collect with Set**: O\(N\) time, O\(N\) space.

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(1, n + 1):
            if nums[i-1] == i:
                pass
            else:
                k = nums[i-1]
                while nums[k-1] != k:
                    j = nums[k-1]
                    nums[k-1] = k
                    k = j
        disappeared = []
        for m in range(1, n+1):
            if nums[m-1] != m:
                disappeared.append(m)
        return disappeared


class SolutionCollectSet:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums) + 1)) - set(nums))


```

