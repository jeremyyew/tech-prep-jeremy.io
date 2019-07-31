'''
- Between two overlapping intervals, we **always pick the one that ends first**, to maximize the amount of time left to pick more intervals. 
- If the intervals are **sorted by end**, then every next `interval` will either end at the same time or later than the `last` one. 
    - If the start of `interval` is before the end of `current`, there is overlap, and we should remove `interval`. 
    - If the start of `interval` is after the end of `current`, there is no overlap, and we can keep `interval`. 
- We sort first so that we only need to compare with the next interval; once we do not have an overlap, all later intervals will also not overlap. We can sort by start or end time, both work. 

'''


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return []
        intervals.sort(key=lambda interval: (interval[1], interval[0]))
        keep = [intervals[0]]
        for interval in intervals[1:]:
            last = keep[-1]
            if last[1] <= interval[0]:
                keep.append(interval)
        return len(intervals) - len(keep)
