from typing import List
from functools import reduce
class SolutionFunc:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # get cumulative product of elements on left, including n
        cumulative_product = lambda acc, n: acc + [acc[-1] * n] 
        left = reduce(cumulative_product, nums, [1])
        left = left[:-1] # we start with 1 and leave out the last element since we really want left[i-1]
        # we reverse so that when we index at i we get everything on the right
        right = (reduce(cumulative_product, reversed(nums), [1]))
        right = list(reversed(right[:-1])) # same thing but we leave out the first element
        print(left)
        print(right)   
        res = []
        for i in range(len(nums)):
            res.append(left[i] * right[i])
        print(res)
        return res

# SolutionFunc().productExceptSelf([1, 2, 3, 4])

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # get cumulative product of elements on left, including n
        left = [1]
        right = [1]
        ln = len(nums)
        for i in range(ln-1):
            left.append(left[-1] * nums[i])
            right.append(right[-1] * nums[(ln - 1) - i])

        right = list(reversed(right)) 
        # print(left)
        # print(right)   
        res = []
        for i in range(len(nums)):
            res.append(left[i] * right[i])
        # print(res)
        return res

# Solution().productExceptSelf([1, 2, 3, 4])