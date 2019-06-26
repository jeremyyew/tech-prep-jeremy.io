# H42-trapping-rain-water

```python
from typing import List 
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        vol = l_max = r_max = 0
        while l < r:
            l_max = max(height[l], l_max)
            r_max = max(height[r], r_max)
            if l_max < r_max: 
                vol += l_max - height[l]
                l += 1
            else: 
                vol += r_max - height[r]
                r -= 1
        return vol
```

