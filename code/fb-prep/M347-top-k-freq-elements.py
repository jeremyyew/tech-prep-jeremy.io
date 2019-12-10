import collections
import heapq


class Solution:
    def topKFrequent(self, nums, k):
        counts = collections.Counter(nums)
        freq_v = [(-freq, value) for value, freq in counts.items()]
        heapq.heapify(freq_v)
        top_k = []
        for _ in range(k):
            _, v = heapq.heappop(freq_v)
            top_k.append(v)
        return top_k


m
