import math
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        l, r = 0, 0
        counts, n = Counter(t), len(set(t))
        window_str, min_l = "", math.inf

        while r < len(s):
            c = s[r]
            if c in counts:
                counts[c] -= 1
                if counts[c] == 0:
                    n -= 1
            r += 1
            while n == 0:
                if r - l < min_l:
                    min_l = r - l
                    window_str = s[l:r]
                c = s[l]
                if c in counts:
                    if counts[c] == 0:
                        n += 1
                    counts[c] += 1
                l += 1
        return window_str


r = Solution().minWindow("ADOBECODBANCC", "AAECC")
print(r)


r = Solution().minWindow("ADOBECODBANCC", "ABCC")
print(r)

r = Solution().minWindow("ADOBECODBANCC", "ABC")
print(r)

r = Solution().minWindow("ADOBECODBANCC", "zz")
print(r)

r = Solution().minWindow("ADOBECODBANCC", "")
print(r)
