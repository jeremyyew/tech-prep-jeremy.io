# M3-longest-substring-without-repeating-characters

{% hint style="info" %}
Use sliding window. Shift `r` until you see a repeat, then flag and shift `l` and remove elements until you've made it unique again. 
{% endhint %}

1. Using sliding-window and counter pattern. Closer to generalized pattern.
2. Using sliding-window and set. Cleaner, but more specific for &gt;1 repeat.

```python
from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, max_l, d = 0, 0, 0, Counter()
        while r < len(s):
            d[s[r]] += 1
            while d[s[r]] > 1:
                d[s[l]] -= 1
                l += 1
            r += 1
            max_l = max(max_l, r-l)
        return max_l

class SolutionSet:
    def lengthOfLongestSubstring(self, s):
        l = r = max_len = 0
        window = set()

        while r < len(s):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            r += 1
            max_len = max(max_len, r - l)
        return max_len


```

