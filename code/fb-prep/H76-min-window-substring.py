from math import inf
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = r = 0  # [1]
        counts = Counter(t)  # [2]
        num_t = len(t)  # [3]
        if not t:
            return ""
        window_str, min_length = "", inf  # [4]

        while r < len(s):  # [5]
            c = s[r]
            if c in counts:
                if counts[c] > 0:
                    num_t -= 1  # [6]
                counts[c] -= 1  # [7], [8]
            r += 1  # [9]
            while num_t == 0:  # [10]
                if r - l < min_length:  # [11]
                    min_length = r - l
                    window_str = s[l:r]
                c = s[l]
                if c in counts:
                    counts[c] += 1  # [12]
                    if counts[c] > 0:
                        num_t += 1
                l += 1  # [13]
        # [14]
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
