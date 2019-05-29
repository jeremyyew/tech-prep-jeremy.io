'''
1. **Collect with counter**: O(N) time, O(N) space.
    Collect in array, scan for missing value.
    We can use Counter to elegantly collect all.

2. **Collect with set**: O(N) time, O(N) space.
    Even more elegant than Counter.

3. **Collect with bitmask**: O(N) time, O(N) space but in bits.
    Assuming we usually use an int or bool for each number (as in Solution 0), those are 24 bytes = 192 bits each in Python. Alternatively we could use a bitmask. Theoretically, we use exactly N bits. So it's O(N/192) space. In practice a binary number in python is min size 34, LOL.

4. **Cyclic Sort**: O(N) time, O(1) space. (Submitted)
    1. Outer loop over `i`.
    2. Inner loop to jump around correcting displacements until we reach a non-displacement, then continue outer loop.
    3. Remember to check for index out-of-bounds at every step; as any number could be `n`.  
    4. Run through again to find missing.  
    4. If there were no missing numbers, then `n` itself is the missing number.  

5. **Gaussian Sum**: O(N) time, O(1) space. Simple, elegant.  
    See below.

6. **XOR**: O(N) time, O(1) space. Elegant.
    - We make use of the fact that `XOR` is commutative to cancel out all values except the missing one i.e. `y XOR y` = 0 and `y XOR y XOR k = k`.
    - The indices of the arrays represent the numbers that should be there.
    - If we 'cancel out' pairs of indices and values that are both present, then we will be left with the indice `k` that is missing the value `k`, as well as the extra value `n` that shouldn't be there.
    - Then we simply have to `XOR n` as well to cancel it out.

    [1] Start with `n`.  
    [2] For each index `i`, `n = n XOR i XOR nums[i]`.  

7. **Binary search**: O(NlogN) time, O(1) space.
    [1] Sort.  
    [2] Binary search to see if value is displaced from corresponding index; find the start of displacement.  
    [3] If `m` displaced, missing on left of `m`, inclusive of `m`.  
    [4] If `m` not displaced, missing on right of `m`, non-inclusive of `m`.  

    Invariant: missing is always in `nums[l:r]`.  
    Termination: we always reduce search area by half, down to 1.  

    With Counting sort: O(N) time, O(N) space.  
    With other sorts: O(NlogN) time, O(1) space.  

See https://leetcode.com/articles/missing-number.
'''
from collections import Counter


class SolutionCollectCounter:
    def missingNumber(self, nums):
        counts = Counter(nums)
        missing = [n for n in range(len(nums)+1) if counts[n] == 0]
        return missing[0]


class SolutionCollectSet:
    def missingNumber(self, nums):
        return list(set(range(len(nums) + 1)) - set(nums))[0]


class SolutionCollectBitMask:
    def missingNumber(self, nums):
        def positionOfSetBit(n):
            i = 1
            pos = 1
            while ((i & n) == 0):
                i = i << 1
                pos += 1
            return pos
        bitmask = 0
        for n in nums:
            bitmask |= (1 << n)
        missing = positionOfSetBit(~bitmask) - 1
        return missing


class Solution:
    def missingNumber(self, nums):
        i, n = 0, len(nums)
        for i in range(n):  # [1]
            if i >= n or nums[i] == i:  # [3]
                pass
            k = nums[i]
            while k < n and k != nums[k]:  # [2], [3]
                j = nums[k]
                nums[k] = k
                k = j
        for i in range(n):  # [4]
            if nums[i] != i:
                return i
        return n  # [5]


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


class SolutionBinarySearch:
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
