'''
- First sort by `h`, and then by `k`. 
- We will insert elements into the queue iteratively from left to right.
- `k` represents the position in the queue that the element `(h, k)` should be in, because everything in the queue is taller than `h`, so we need `k` number of people on the left of `(h, k)`. 
- O(N^2) time due to shifting of elements from insert. 
'''


class Solution:
    def reconstructQueue(self, people):
        people.sort(key=lambda p: (-p[0], p[1]))
        queue = []
        for p in people:
            queue.insert(p[1], p)
        return queue
