# H295-find-median-from-data-stream

1. Sort on demand: O\(NlogN\) time, O\(N\) space.
2. Keep it sorted \(insertion sort\): O\(N + logN = N\) time, O\(N\) space.
3. Two Heaps: O\(logN\) time, O\(N\) space.

    Balance a MaxHeap `lo` and MinHeap `hi`. Invariants: `lo` and `hi` are always equal length. Variable `median` is always the correct median value \(when `N` is odd it represents the median element itself, when `N` is even it represents the average of the two middle values\).

   1. If `N` is even, then for the next element, we insert into the heap that it belongs to, and the new median is the min/max of that heap. 
   2. If `N` is odd, then shift both `median` and `num` into the correct heap, and get the average of the min of `hi` and the max of `lo`. 

```python
import heapq

class MinHeap():
    def __init__(self): self.h = []

    def push(self, x): heapq.heappush(self.h, x)

    def pop(self): return heapq.heappop(self.h)

    def peek(self): return self.h[0]


class MaxHeap():
    def __init__(self): self.h = []

    def push(self, x): heapq.heappush(self.h, -x)

    def pop(self): return -(heapq.heappop(self.h))

    def peek(self): return -self.h[0]


class MedianFinder(object):

    def __init__(self):
        self.median = None
        self.hi = MinHeap()
        self.lo = MaxHeap()
        self.len = 0

    def addNum(self, num):
        if self.median is None:
            self.median = num
        elif self.len % 2 == 0:
            if num > self.median:
                self.hi.push(num)
                self.median = self.hi.pop()
            else:
                self.lo.push(num)
                self.median = self.lo.pop()
        else:
            if num > self.median:
                self.hi.push(num)
                self.lo.push(self.median)
            else:
                self.hi.push(self.median)
                self.lo.push(num)
            self.median = (self.hi.peek() + self.lo.peek()) / 2
        self.len += 1

    def findMedian(self):
        return self.median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

```

