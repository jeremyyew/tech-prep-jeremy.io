# M3-longest-substring-without-repeating-characters

Adapted from [https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/](https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/).

1. Brute force: search for repeat characters in current sequence. 

   * Constantly checking entire substring for every new r.
   * O\(N^2\) time and O\(N\) space.

2. Set Window. 
   * \[1\] No need to search the whole current substring. Store window as set. 
   * \[2\] If there is a repeat element, don't have to find index. Just remove element s\[l\] and start again with l+1.
   * r traverses all elements exactly once. l traverses all elements at most once. So O\(N\) time. O\(N\) space for set \(or O\(min\(k,N\)\) where k is the set of distinct characters.

```python
class Solution:
    def lengthOfLongestSubstring(self, s):
        N = len(s)
        if N <= 1:
            return N
        l = r = max_len = 0
        window = set()  # [1]
        while r < N:
            if s[r] in window:  # [2]
                window.remove(s[l])
                l += 1
            else:
                window.add(s[r])
                r += 1
                max_len = max(max_len, r - l)
        return max_len


class SolutionBruteForce:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        if N <= 1:
            return N
        max_len = 0
        l, r = 0, 1
        while r < N:
            for i in range(l, r):
                if s[i] == s[r]:
                    l = i + 1
            r += 1
            max_len = max(max_len, r - l)
            print(l, r)
        return max_len


# print(Solution().lengthOfLongestSubstring("abcabcbb"))


# print(Solution().lengthOfLongestSubstring("abcabcbb"))

```

