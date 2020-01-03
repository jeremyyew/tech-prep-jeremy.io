# M139-word-break

_Given a **non-empty** string s and a dictionary wordDict containing a list of **non-empty** words, determine if s can be segmented into a space-separated sequence of one or more dictionary words._

_**Note:**_

* _The same word in the dictionary may be reused multiple times in the segmentation._
* _You may assume the dictionary does not contain duplicate words._

_**Example 1:**_

```text
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
```

_**Example 2:**_

```text
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
```

_**Example 3:**_

```text
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
```

1. Brute Force? 

    Test all combinations of words that are equal to the length of s. 

2.  Let OPT\(i\) be the possibility of segmenting the prefix of s of length i, and s\[:i\] be the substring from 0 to i \(non-inclusive\). Then, for OPT\(i\) to be true, 
   1. there exists some word that is a suffix of s\[:i\] 
   2. we can segment the remaining prefix s\[:i-w\], i.e. OPT\(i-w\) is true 
   3. the word is not longer than the substring itself \(ensured by 1\), else we get negative indexes.

Formally, `OPT(i) = s[:i].endswith(word) and i >= w and OPT(i - w)` for some word in wordDict with length w.

```python
from typing import List



class Solution:
    def wordBreakRec(self, s, d):
        
    
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

