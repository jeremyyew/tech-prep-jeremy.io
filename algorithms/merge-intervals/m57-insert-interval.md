# M57-insert-interval

* We present a simple linear solution. 
* It is possible to do binary search, but deceivingly tricky to decide what to return or the indexes to insert at.  

```python
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

```

