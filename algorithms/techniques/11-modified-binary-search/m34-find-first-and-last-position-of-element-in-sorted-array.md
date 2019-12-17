# M34-find-first-and-last-position-of-element-in-sorted-array

Simply do two modified binary searches, one to find the first occurence and the other, the last occurence. We could also do two binary searches from the first occurence we find, but its still going to be O\(logN\).

Linearly scanning from our first occurence is O\(N\) since all the elements might be the target.

```python
class Solution:
    def searchRange(self, nums, target):
        LEFT, RIGHT = 0, 1
        def searchModified(direction):
            t = -1
            l, r = 0, len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if target == nums[m]:
                    t = m
                    if direction == RIGHT:
                        l = m + 1
                    else:
                        r = m - 1
                elif target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            return t
        lo = searchModified(LEFT)
        hi = searchModified(RIGHT)
        return [lo, hi]

```

