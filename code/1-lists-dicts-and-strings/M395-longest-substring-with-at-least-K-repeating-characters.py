'''
1. Get `ltk`, the list of characters that appear less than `k` times in `s`.
2. Base case: There are no `ltk` chars in `s`, so `s` is a valid string.
3. Take note we should use length to force evaluation of `ltk` instead of boolean coercion, since list comprehension gives a generator object which evaluates to `True`.
4. Inductive case: A valid substring will never contain any of `ltk`. So one of the substrings that does not contain any of `ltk` will contain the max. So split `s` by all chars in `ltk`; for each of these substrings, get its local max length, and get the max of these.
5. Use `re.split()` to split by multiple chars. This is better than splitting single chars at a time as per Stefan's solution.
6. Use `join()`` to obtain the delimiter expression.

## Time complexity: O(N)
For each recursive call we take O(N) to count all elements of substring s, and check which ones are less than k. The combined work of a set of recursive calls from sis at most O(N), since we are counting elements of substrings.
Each time we split, each substring has at least one less unique less-than-k character, and we only have 26 unique lowercase letters; so the maximum level of recursion is 26. So O(26N) = O(N). 

Adapted from https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/87768/4-lines-Python
'''

import re
import collections


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        ltk = [c for c, count in collections.Counter(
            s).items() if count < k]  # [1]
        if len(ltk) == 0:  # [2], [3]
            return len(s)
        # [4], [5], [6]
        return max(self.longestSubstring(t, k) for t in re.split('|'.join(ltk), s))
