from math import inf
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # [1] Begin with l and r as 0.
        l = r = 0
        # [2] We will need to keep track of whether we have accounted for  seen so far; in t in dict `counts` using built-in `Counter` class.
        counts = Counter(t)
        # [3] When the total count is zero, we have accounted for all elements in t with the current window. But instead of repeatedly summing, we will just keep track of the total number of elements in t accounted for so far, so once it's zero we know we have a valid window.
        num_t = len(t)
        # [4] We will also keep track of the length and start point of the minimum-length valid window so far.
        head, min_length = 0, inf

        # [5] What we want is to shift r until we get a valid window, and then try to shorten that window by shifting l until our window is invalid, and then continue shifting r again until we get the next valid window. So our terminating condition for shifting r will be r < len(s).
        while r < len(s):
            # [6] If the current element `e` is an element we still need, we account for the fact that we obtained it by decrementing `num_t`.
            if s[r] in counts:
                if counts[s[r]] > 0:
                    num_t -= 1
                # [7] But whether or not we actually needed `e`, we should account for seeing it by decrementing `e`'s count. The negative count helps us keep track of extra `e`'s that we can later safely leave out of a window.
                # [8] Note we increment the element `e`'s count only if it is actually a member of `t`. Technically this will work even if we don't check if the key exists, because `Counter` happens to default zero for any new key, and this also wouldn't affect the semantics of the solution because non-keys will never grow past zero, and thus will not affect `num_t`. However in this implementation we only manipulate the keys that exist in `t` - I find it easier to reason about, and this way `counts` uses only as much space as we need.
                counts[s[r]] -= 1
            # [9] Now we increment r for the next trial. We can happily use r for length calculations within this trial though, due to zero-indexing; just keep this in mind.
            r += 1
            # [10] After every `r` shift we will check if we have achieved a valid window i.e. `num_t == 0`. If we have, then we begin shifting `l`, until we get invalid window i.e. `num_t > 0`.
            while num_t == 0:
                # [11] If we have achieved a new min length, save its value and the window's starting point.
                if r - l < min_length:
                    min_length = r - l
                    head = l
                # [12] We now do the opposite of [6] and [7]. For some element `e` that we needed for a valid window, whether or not we had spare elements `e` in the window, we account for seeing it by incrementing its count. If we had any spares we would be decrementing a negative number and be safe. Else if we had no spares, we will now have one `e` unaccounted for.
                if s[l] in counts:
                    counts[s[l]] += 1
                    if counts[s[l]] > 0:
                        num_t += 1
                # [13] And now we increment l for the next trial.
                l += 1
        # [14] If we didn't record any min lengths, we didn't find any valid windows. Else, return the min-length valid window derived from its head and its length.
        return '' if min_length == inf else s[head:head+min_length]
