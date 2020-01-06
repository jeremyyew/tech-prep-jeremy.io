---
description: 'https://leetcode.com/problems/largest-rectangle-in-histogram/'
---

# H84-largest-rectangle-in-histogram

_Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram._

_**Example:**_

```text
Input: [2,1,5,6,2,3]
Output: 10
```

* [https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28917/AC-Python-clean-solution-using-stack-76ms](https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28917/AC-Python-clean-solution-using-stack-76ms)

```python
def largestRectangleArea(height):
    height.append(0)
    stack = [-1]
    ans = 0
    for i in range(len(height)):
        while height[i] < height[stack[-1]]:
            h = height[stack.pop()]
            w = i - stack[-1] - 1
            ans = max(ans, h * w)
            stack.append(i)
    height.pop()
    return ans


print(largestRectangleArea([7, 1, 5, 6, 4]))
```

