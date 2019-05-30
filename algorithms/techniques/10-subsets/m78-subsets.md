# M78-subsets

1. Iterative
2. Iterative w `itertools.combinations`
3. Recursive
4. Tail-recursive

```python
from itertools import combinations
class Solution():
    def subsets(self, nums):
        subs = [[]]
        for n in nums:
            subs = subs + [sub + [n] for sub in subs]
        return subs


class SolutionItertools():
    def subsets(self, nums):
        subs = []
        for n in range(len(nums) + 1):
            subs += list(combinations(nums, n))
        return subs


class SolutionRecursive():
    def subsets(self, nums):
        if nums == []:
            return [[]]
        prev = self.subsets(nums[:-1])
        return prev + [subset + [nums[-1]] for subset in prev]


class SolutionTailRecursive():
    def subsets(self, nums):
        def subsetsRec(i, acc):
            if i == len(nums):
                return acc
            return subsetsRec(i+1, acc + [subset + [nums[i]] for subset in acc])
        return subsetsRec(0, [[]])
```

