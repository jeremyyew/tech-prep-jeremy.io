# M11-container-with-most-water

```python
'''
[1] Start with two pointers on the ends as container with max value. 
[2] Get new values by shifting the shorter end inwards.


- The intuition is that shifting the taller end will never get us higher area, but shifting the shorter end might. 
- The current value is the max value for any container with the shorter end. 

'''


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        l, r = 0, len(height) - 1  # [1]
        while l < r:
            # [2]
            minHeight = min(height[l], height[r])
            width = r - l
            area = minHeight * width
            maxArea = max(area, maxArea)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return maxArea

```

