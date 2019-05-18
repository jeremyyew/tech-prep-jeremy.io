'''
See https://leetcode.com/articles/missing-number.

0. Brute force: O(N) time, O(N) space. 
    Collect in array, scan for missing value. 
    Alternatively we could use a bitmask, which gives us roughly O(1) space as long as N <= bits of an int (and reduces traversal by half since we can just XOR bitmask with 1111...). 

1. Gaussian Sum: O(N) time, O(1) space. Simple, elegant. 
    See below. 

2. XOR: O(N) time, O(1) space. Elegant. 
    - We make use of the fact that XOR is commutative to cancel out all values except the missing one i.e. y XOR y = 0 and y XOR y XOR k = k. 
    - The indices of the arrays represent the numbers that should be there. 
    - If we 'cancel out' pairs of indices and values that are both present, then we will be left with the indice k that is missing the value k, as well as the extra value n that shouldn't be there. 
    - Then we simply have to XOR n as well to cancel it out. 

    [1] Start with n.  
    [2] For each index i, n = n XOR i XOR nums[i].

3. Binary search displacement by index: O(NlogN) time, O(1) space.
    [1] Sort. 
    [2] Binary search to see if value is displaced from corresponding index; find the start of displacement.  
    [3] If m displaced, missing on left of m, inclusive of m.
    [4] If m not displaced, missing on right of m, non-inclusive of m.

    Invariant: missing is always in nums[l:r]. 
    Termination: we always reduce search area by half, down to 1. 
    
    Counting sort: O(N) time, O(N) space. 
    With other sorts: O(NlogN) time, O(1) space.
'''


class Solution:
    def missingNumber(self, nums):
        nums.sort()  # [1]
        l, r = 0, len(nums)
        while l < r:  # [2]
            m = (l + r) // 2
            if nums[m] > m:
                r = m  # [3]
            else:
                l = m + 1  # [4]
        return l


class SolutionGaussianSum:
    def missingNumber(self, nums):
        n = len(nums)
        return n*(n+1)//2 - sum(nums)


class SolutionXOR:
    def missingNumber(self, nums):
        n = len(nums)  # [1]
        for i, num in enumerate(nums):
            n ^= i ^ num  # [2]
        return n
