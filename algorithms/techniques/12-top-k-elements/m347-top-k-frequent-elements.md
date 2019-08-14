# M347-top-k-frequent-elements

```python
import heapq
import collections


class Solution:
    def topKFrequent(self, nums, k):
        count = collections.Counter(nums)
        count = [(-freq, value) for value, freq in count.items()]
        heapq.heapify(count)
        top_k = [heapq.heappop(count) for _ in range(k)]
        return [value for neg_freq, value in top_k]

```

