# M47-permutations-II

* Build the set of permutations up iteratively. 
* Since its a set, duplicates \(caused by repeated elements\) will be ignored at every step.
* Use tuples instead of lists, since lists are not hashable. 
* Time complexity: greater than O\(\(N - K\)!\) where K is number of duplicates. 

```python
from functools import reduce
from typing import List
import itertools

class Solution:
    '''Given all permutations of a set `s`, we can obtain all permutations of `s` + `k` by inserting `k` into all positions of every permutation.'''

    def permuteUnique(self, nums):
        return reduce(lambda perms, n: {p[:i] + (n,) + p[i:]
                                        for p in perms
                                        for i in range(len(p)+1)},
                      nums, {()}) if nums else []


# r = Solution().permuteUnique([1, 1, 2])
# print(r)

```

