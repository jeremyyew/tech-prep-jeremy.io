# M56-merge-intervals

{% hint style="info" %}
**Sort first, then merge sequentially.** 
{% endhint %}

1. Brute force: compare every interval with every other, merge if overlap.
2. Sort and merge iteratively: sort first will allow us to merge contiguous intervals at once.
   * `SolutionInitial` uses indexing, a bit messy.  
   * `Solution` uses iteration, and looks at last member of `merged` \(as opposed to previous index in `intervals`\) to retrieve previous interval to merge with. Adapted from provided solution. 

```python
from typing import List
class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if merged and merged[-1][1] >= interval[0]:
                merged[-1][1] = max(merged[-1][1], interval[1])
            else:
                merged.append(interval)
        return merged


class SolutionInitial:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        merged = []
        intervals.sort(key=lambda x: x[0])
        start, end = intervals[0]
        i = 1
        while i < len(intervals):
            next_start, next_end = intervals[i]
            if next_start <= end:
                start, end = start, max(end, next_end)
            else:
                merged.append([start, end])
                start, end = next_start, next_end
            i += 1
        merged.append([start, end])
        return merged


# r = Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]])
# print(r)

```

