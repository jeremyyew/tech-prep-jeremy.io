# H76-minimum-window-substring

{% hint style="info" %}
* The key idea is to **shift `r` until we get a valid window, and then try to shorten that window by shifting `l` until our window is invalid**, and then continue shifting `r` again until we get the next valid window. 
* Use a **counter** to keep track of elements we need to account for, **decrementing them when they are added** to a window. 
* Decrement them **past zero** to represent **extra elements.** 
* **Do the reverse when leaving elements out** of our window, incrementing their count and then checking if we now need them or if we had spares. 
{% endhint %}

### Full walkthrough: 

1. Begin with `l` and `r` as 0.
2. We will need to keep track of the elements in `t` we need to account for, so we use the built-in `Counter` class.
3. When the total count is zero, we have accounted for all elements in `t` with the current window. But instead of repeatedly summing, we will just keep track of the total number of elements in `t` accounted for so far, so once it's zero we know we have a valid window.
4. We will also keep track of the length and start point of the minimum-length valid window so far.
5. Our terminating condition for shifting `r` will be `r < len(s)`.
6. If the current element `e` is an element we still need, we account for the fact that we obtained it by decrementing `num_t`.
7. But whether or not we actually needed `e`, we should account for seeing it by decrementing `e`'s count. The negative count helps us keep track of extra `e`'s that we can later safely leave out of a window.
8. Note we increment the element `e`'s count only if it is actually a member of `t`. Technically this will work even if we don't check if the key exists, because `Counter` happens to default zero for any new key, and this also wouldn't affect the semantics of the solution because non-keys will never grow past zero, and thus will not affect `num_t`. However in this implementation we only manipulate the keys that exist in `t`; I find it easier to reason about, and this way `counts` uses only as much space as we need.
9. Now we increment `r` for the next trial. We can happily use `r` for length calculations within this trial though, due to zero-indexing; just keep this in mind.
10. After every `r` shift we will check if we have achieved a valid window i.e. `num_t == 0`. If we have, then we begin shifting `l`, until we get invalid window i.e. `num_t > 0`.
11. If we have achieved a new minimum length, save its value and the window's starting point.
12. We now do the opposite of \[6\] and \[7\]. For some element `e` that we needed for a valid window, whether or not we had spare elements `e` in the window, we account for seeing it by incrementing its count. If we had any spares we would be decrementing a negative number and be safe. Else if we had no spares, we will now have one `e` unaccounted for, which we must register by incrementing `num_t`.
13. And now we increment `l` for the next trial.
14. And finally if we didn't record any minimum lengths, we didn't find any valid windows. Else, return the minimum-length valid window derived from its head and its length.

Adapted from [https://leetcode.com/problems/minimum-window-substring/discuss/26808/Here-is-a-10-line-template-that-can-solve-most-'substring'-problems](https://leetcode.com/problems/minimum-window-substring/discuss/26808/Here-is-a-10-line-template-that-can-solve-most-'substring'-problems). 

```python
from math import inf
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = r = 0  # [1]
        counts = Counter(t)  # [2]
        num_t = len(t)  # [3]
        head, min_length = 0, inf  # [4]

        while r < len(s):  # [5]
            if s[r] in counts:
                if counts[s[r]] > 0:
                    num_t -= 1  # [6]
                counts[s[r]] -= 1  # [7], [8]
            r += 1  # [9]
            while num_t == 0:  # [10]
                if r - l < min_length:  # [11]
                    min_length = r - l
                    head = l
                if s[l] in counts:
                    counts[s[l]] += 1  # [12]
                    if counts[s[l]] > 0:
                        num_t += 1
                l += 1  # [13]
        return '' if min_length == inf else s[head:head+min_length]  # [14]

```

