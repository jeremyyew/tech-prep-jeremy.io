# M152-maximum-product-subarray

```python
from typing import List

''' 
- The difference between this and maximum subarray is that a 'small' number (negative with high magnitude) may still become a 'big' number later by multiplication with a new negative number. 
- So, we always need to keep both the biggest and the smallest number so far. 
- For the next subarray that includes n, n*big is not always bigger than big. Not only might n > n*big, we may also get n*small > n and n*big. See below for explanation of all cases. 

[1] In the base case: maximum, big, small is nums[0].
[2] In the induction case: compare n, n*big, n*small to get new big and new small.
[3] The new max is either the old max or the new big. 
[4] You should declare the new big and small as a tuple. We evaluate both before assigning both. Otherwise, if we do one by one, then after the first assignment we lose the old value which we needed for the second computation. Otherwise we will have to use temp variables.
'''


class Solution:
    def maxProduct(self, nums: List[int]):
        big = small = maximum = nums[0]  # [1]
        print(big, small, maximum)
        for n in nums[1:]:
            big, small = max(n, n*big, n*small), min(n,
                                                     n*big, n*small)  # [2], [4]
            maximum = max(maximum, big)  # [3]
        return maximum


r = Solution().maxProduct([-4, -3, -2])
print(r)


'''
- There are two main cases to demonstrate when n*small or n may be larger than n*big.  
    If n > 0:
        Then big >= small -> n*big >= n*small is always true. 
        If big > 0: 
            Then n*big > n. 
            So n*big is max. 
        Else if big <= 0: 
            Then n > n*big. 
            So n is max.
    If n <= 0:
        Either big and small swap signs (big > 0 and small <0), or small will be hit less badly (both > 0), or small will be flipped further positive (both <0). 
        So big >= small -> n*big <= n*small is always true. 
        If small > 0: 
            Then n*small <= n. 
            So n is max. 
        If small <= 0: 
            Then n*small >= n. 
            So n*small is max. 
'''

```

