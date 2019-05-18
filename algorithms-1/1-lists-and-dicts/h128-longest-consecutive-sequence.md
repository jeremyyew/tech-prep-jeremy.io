# H128-longest-consecutive-sequence

Adapted from https://leetcode.com/problems/longest-consecutive-sequence/solution/.

0. **Brute force:** counting up from every number in list. 
    We count up and stop when n+1 isnt in the list. 
    Not only does every lookup take O(N) since we look through the entire list, we might we repeat a sequence already found [2,3,4] when counting from 1. So O(N^2).
    
    So we need a way to lookup quicker, and to not repeat sequences. 


1. **Smart Count:** Counting up from every number in set,
    [1] Get set of nums. 
    [2] For every num, count up. 
    [3] TRICK: But if num-1 exists, don't start counting. This implies num is part of some other sequence, that we either have counted, or will eventually count. 

2. **Sequence Dictionary:** Updating and merging sequences stored in dicts
    - We store a dict of consecutive sequences, which each have length and point to the left and right of the entire sequence they are connected to. 
    - For every num, we check if num-1 and num+1 are present in the dict. If they are, we can find the left and right of a sequence that num can be connected to. Then, either we append num to the left, to the right, or merge two sequences.
    - We can always assume any edge element has updated information, because either they added themselves or they were updated by the other end. 

    [1] If we've seen it, do nothing.  
    [2] If both num+1 and num-1 are present, merge the two by updating the left and right.  
    [3] If only num+1 is present, append to the left by updating num and r.  
    [4] If only num-1 is present, append to the right by updating l and num.  
    [5] If neither num+1 or num-1 are present, just register num as length, left, right = 1, num, num.  
    [6] For case [2], we want to update num, l and r.  
        For case [3], l = num so seen[l] = seen[num].  
        For case [4], r = num so seen[r] = seen[num].  
        For case [5], the seen[l] and seen[r] do nothing.  

```python
from typing import List


class Solution:
    def longestConsecutive(self, nums):
        max_streak = 0
        num_set = set(nums)  # [1]
        for num in num_set:
            if num - 1 in num_set:  # [3]
                continue
            current = num
            streak = 1
            while current + 1 in num_set:  # [2]
                current += 1
                streak += 1
            max_streak = max(max_streak, streak)
        return max_streak


class SolutionBruteForce:
    def longestConsecutive(self, nums):
        longest_streak = 0

        for num in nums:
            current_num = num
            current_streak = 1

            while current_num + 1 in nums:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

        return longest_streak


class SolutionUpdateMerge:
    def longestConsecutive(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 1:
            return N
        seen = {}
        for num in nums:
            if num in seen:  # [1]
                continue

            length, l, r = 0, num, num

            if num+1 in seen and num-1 in seen:  # [2]
                l_length, l, _ = seen[num-1]
                r_length, _, r = seen[num+1]
                length = l_length + r_length

            elif num+1 in seen:  # [3]
                length, _, r = seen[num+1]
                l = num

            elif num-1 in seen:  # [4]
                length, l, _ = seen[num-1]
                r = num

            seen[num] = seen[l] = seen[r] = length + 1, l, r  # [5]
        print(seen)
        return max([length for length, l, r in seen.values()])


# print(Solution().longestConsecutive([-9, -4, 9, -7, 0, 7, 3, -1, 6,
#                                      2, -2, 8, -2, 0, 2, -7, -5, -2, 6, -5, 0, -8, 8, 1, 0, 6, 8, -8, -1]))

```

