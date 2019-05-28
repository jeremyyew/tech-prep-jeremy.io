import itertools
from typing import List


# My version of someone else's solution below. For modularity, I abstract the two-sum scan, and pass it an array slice instead of indices.
# We simply require the twoSum to return the values that add up to the target (instead of indices), with no duplicates, and it cannot assume sorted values in general. Keep in mind we must also give it the complement of the target, not the target itself, since we are aiming for zero-sum.

class Solution(object):
    # Scans sorted array nums from left and right to find two numbers that sum to the the target, i.e. so that we have a zero sum. We know it is better to sort once in threeSum, so we don't re-sort here - this is an optimization which doesn't break modularity, since we don't necessarily assume sorted for other twoSums.
    # Also skips repeated numbers, so we won't have duplicates.
    def twoSum(self, target, nums):
        # nums.sort()
        res = []
        l = 0
        r = len(nums) - 1
        while l < r:
            diff = nums[l] + nums[r] - target

            if diff < 0:  # [3]
                l += 1
            elif diff > 0:  # [4]
                r -= 1
            else:  # [5]
                res.append([nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]:  # [6]
                    l += 1
                while l < r and nums[r] == nums[r-1]:  # [6]
                    r -= 1
                l += 1
                r -= 1
        return res

    def threeSum(self, nums):
        res = []
        nums.sort()
        length = len(nums)
        for i in range(length-2):  # [8]
            if nums[i] > 0:
                break  # [7]
            if i > 0 and nums[i] == nums[i-1]:
                continue  # [1]
            # We need to make target negative since we are trying to find the twoSum of its complement, so that target + x + y = 0.
            target = nums[i]
            # Set the appropriate l index. r-index will always be the same. # [2]
            res_i = self.twoSum(-target, nums[i+1:])
            # To demonstrate modularity:
            # res_i = twoSumWithDict(-target, nums[i+1:])

            # Include the target.
            res += [(target, x, y) for x, y in res_i]
        return res


def twoSumWithDict(target, nums):
    # One pass with hash. Includes duplicate pairs but not equivalent combinations.
    comps = {}
    res = set()
    # print(target, nums)
    for i in range(len(nums)):

        x = nums[i]
        if x in comps:
            res.add((comps[x], x))
        else:
            comps[target - x] = x
    return [list(twoSum) for twoSum in res]


# https://leetcode.com/problems/3sum/discuss/232712/Best-Python-Solution-(Explained)
'''
We select a target, and find two other numbers which make total zero.
For those two other numbers, we move pointers, l and r, to try them.

First, we sort the array, so we can easily move i around and know how to adjust l and r.
If the number is the same as the number before, we have used it as target already, continue. [1]
We always start the left pointer from i+1 because the combination of 0~i has already been tried. [2]

Now we calculate the total:
If the total is less than zero, we need it to be larger, so we move the left pointer. [3]
If the total is greater than zero, we need it to be smaller, so we move the right pointer. [4]
If the total is zero, bingo! [5]
We need to move the left and right pointers to the next different numbers, so we do not get repeating result. [6]

We do not need to consider i after nums[i]>0, since sum of 3 positive will be always greater than zero. [7]
We do not need to try the last two, since there are no rooms for l and r pointers.
You can think of it as The last two have been tried by all others. [8]
'''


class SolutionExample(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        length = len(nums)
        for i in range(length-2):
            if nums[i] > 0:
                break  # [7]
            if i > 0 and nums[i] == nums[i-1]:
                continue  # [1]

            l, r = i+1, length-1  # [2]
            while l < r:
                total = nums[i]+nums[l]+nums[r]

                if total < 0:  # [3]
                    l += 1
                elif total > 0:  # [4]
                    r -= 1
                else:  # [5]
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:  # [6]
                        l += 1
                    while l < r and nums[r] == nums[r-1]:  # [6]
                        r -= 1
                    l += 1
                    r -= 1
        return res

# This is brute force, takes O(nC3). Too slow on large inputs.
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         threeSums = set()
#         threeCombs = itertools.combinations(nums, 3)
#         for threeTuple in threeCombs:
#             if sum(threeTuple) == 0:
#                 # We convert to list to sort it, so different combinations are equivalent. We then convert back to tuple since we need it to be hashable to be addable to the set.
#                 threeSums.add(tuple(sorted(list(threeTuple))))

#         return list(threeSums)


# res = Solution().threeSum([-1, 0, 1, 2, -1, -4])
# print(res)
