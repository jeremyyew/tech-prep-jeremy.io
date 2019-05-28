'''
- We present a simple linear solution. 
- It is possible to do binary search, but deceivingly tricky to decide what to return or the indexes to insert at.  
- An attempt is done below. 
'''
from typing import List


class SolutionLinear:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def overlap(a, b) -> bool:
            return not (before(a, b) or after(a, b))

        def before(a, b) -> bool:
            return a[1] < b[0]

        def after(a, b) -> bool:
            return a[0] > b[1]

        def merge(a, b) -> List[int]:
            return([min(a[0], b[0]), max(a[1], b[1])])
        # [1] Base case []: immediately return `newInterval`.
        if not intervals:
            return [newInterval]
        merged = []
        i = 0
        while i < len(intervals):
            if before(newInterval, intervals[i]):
                break
            if overlap(newInterval, intervals[i]):
                newInterval = merge(newInterval, intervals[i])
            else:
                merged.append(intervals[i])
            i += 1
        merged += [newInterval] + intervals[i:]
        return merged

        # class Solution:

        #     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #         def overlap(a, b) -> bool:
        #             return not (before(a, b) or after(a, b))

        #         def before(a, b) -> bool:
        #             return a[1] < b[0]

        #         def after(a, b) -> bool:
        #             return a[0] > b[1]

        #         def merge(a, b) -> List[int]:
        #             return([min(a[0], b[0]), max(a[1], b[1])])

        #         # [1] Base case []: immediately return `newInterval`.
        #         if not intervals:
        #             return [newInterval]

        #         # [2] Get rid of edge cases where `newInterval` is before the first or after the last interval, so later we may consider less.
        #         if before(newInterval, intervals[0]):
        #             return [newInterval] + intervals
        #         if after(newInterval, intervals[-1]):
        #             return intervals + [newInterval]

        #         l, r = 0, len(intervals) - 1
        #         # [2] Binary search to find the first possible insertion start point.
        #         while l <= r:
        #             if l == r:
        #                 if before(newInterval, intervals[l]):
        #                     l = r = l - 1
        #                     break
        #                 elif after(newInterval, intervals[l]):
        #                     l = r = l + 1
        #                     break
        #             m = (l + r) // 2
        #             if before(newInterval, intervals[m]):
        #                 r = m
        #             elif after(newInterval, intervals[m]):
        #                 l = m+1
        #             else:
        #                 if newInterval[1] <= intervals[m][1]:
        #                     r = m
        #                 if newInterval[0] >= intervals[m][0]:
        #                     l = m
        #         while r < len(intervals):
        #             if overlap(intervals[r], newInterval):
        #                 newInterval = merge(intervals[r], newInterval)
        #                 break
        #             r += 1
        #         print(l, r)
        #         return (intervals[:l+1]) + [newInterval] + intervals[r:]

        # r = Solution().insert([[2, 6], [7, 9]], [15, 18])
        # print(r)
