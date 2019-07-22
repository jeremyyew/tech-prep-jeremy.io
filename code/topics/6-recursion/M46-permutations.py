from typing import List
import itertools
from functools import reduce


class SolutionItertools:
    def permute(self, nums):
        return list(itertools.permutations(nums))


class Solution:
    '''Given all permutations of a set `s`, we can obtain all permutations of `s` + `k` by inserting `k` into all positions of every permutation.'''

    def permute(self, nums):
        return reduce(lambda perms, n: [p[:i] + [n] + p[i:]
                                        for p in perms for i in range(len(p)+1)],
                      nums, [[]])


class SolutionIterativeBottomUp:
    '''Given all permutations of a set `s`, we can obtain all permutations of `s` + `k` by inserting `k` into all positions of every permutation.'''

    def permute(self, nums):
        perms = [[]]
        for n in nums:
            perms = [[p[:i] + [n] + p[i:]]
                     for p in perms
                     for i in range(len(p)+1)]
        return perms


class SolutionRecBottomUp:
    '''Given all permutations of a set `s`, we can obtain all permutations of `s` + `k` by inserting `k` into all positions of every permutation.'''

    def permute(self, nums):
        return nums and [p[:i] + [nums[0]] + p[i:]
                         for p in self.permute(nums[1:])
                         for i in range(len(nums))] or [[]]


class SolutionRecTopDown:
    '''To obtain all permutations of a set `s`, for each element `k` we get all permutations that start with that element.'''

    def permute(self, nums):
        return [[n] + p
                for i, n in enumerate(nums)
                for p in self.permute(nums[:i] + nums[i+1:])] or [[]]
