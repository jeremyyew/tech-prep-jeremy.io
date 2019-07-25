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