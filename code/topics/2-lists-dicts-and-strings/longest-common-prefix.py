'''
Brute force: go through all strings, keeping track of longest prefix so far. We can stop if we get empty prefix. 
We sort the strings in lexicographic order (unknown complexity). 
Then we know that the common prefix between the first and the last string is the longest possible, because any prefix built from previous subset of strings cannot be longer (following strings have same or greater number of different characters). 
'''

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        ans = ""
        for a, b in zip(strs[0], strs[-1]):
            if a != b:
                break
            ans += a
        return ans
