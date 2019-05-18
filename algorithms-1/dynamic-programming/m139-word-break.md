# M139-word-break

```python
'''

1. Brute Force? 
    Test all combinations of words that are equal to the length of s. 

2.
    Let OPT(i) be the possibility of segmenting the prefix of s of length i, and s[:i] be the substring from 0 to i (non-inclusive). 
    Then, for OPT(i) to be true, 
    1. there exists some word that is a suffix of s[:i]
    2. we can segment the remaining prefix s[:i-w], i.e. OPT(i-w) is true
    3. the word is not longer than the substring itself (ensured by 1), else we get negative indexes. 

    Formally, 
    OPT(i) = s[:i].endswith(word) and i >= w and OPT(i - w) for some word in wordDict with length w.
'''
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        S = len(s)
        OPT = [False] * (S + 1)
        OPT[0] = True
        for i in range(1, S+1):
            for word in wordDict:
                w = len(word)
                if s[:i].endswith(word) and OPT[i - w]:
                    OPT[i] = True
                    break
        print(OPT)
        return OPT[S]


# r = Solution().wordBreak("leetcode", ["leet", "code"])
# print(r)

```

