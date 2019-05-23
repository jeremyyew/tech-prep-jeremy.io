# M516-longest-palindromic-subsequence

{% hint style="info" %}
For each new element, traverse the string backwards looking for elements to form new symmetries with, deriving the new length from the length of inner palindromes. **Start from `0`, and every time you shift `i` to the right, shift `j` backwards from `i-1` to `0`.**
{% endhint %}

1. Let `dp(j, i)` be the length of the longest palindromic subsequence \(LPS\) from `j` to `i` inclusive. Then, for `s[j:i+1]`, if `s[j] == s[i]`, we have the chance to make a new LPS, so we may add two elements \(`i` and `j`\) to the LPS length from `j+1` to `i-1`, i.e. `dp(j+1, i-1)`.  
2. Else, `dp(j,i)` is either the length of some previous LPS `dp(j, i-1)` \(which may be either the length of some previous LPS that included `s[j]`, or some LPS between `j+1` to `i-1`\), or some new inner LPS between `j+1` and `i`, that includes `s[i]`. Thus `dp(j, i)` is the max of the previous value `dp(j, i-1)` and new value `dp(j+1, i)`.

Formally,

```python
if s[j] == s[i]: 
    dp(j, i) = 2 + dp(j+1, i-1) 
else: 
    dp(j, i) = max(dp(j, i-1), dp(j+1, i))
```

Time complexity is O\(N^2\).

The implementation here uses O\(N\) space instead of O\(N^2\), so the recurrence relation is not clearly reflected in the indexing in the code; we save the previous row of values `dp(j, i-1)` as `prev`.

Adapted from [https://leetcode.com/problems/longest-palindromic-subsequence/discuss/99117/Python-standard-DP-beats-100-\(with-"pre-processing"](https://leetcode.com/problems/longest-palindromic-subsequence/discuss/99117/Python-standard-DP-beats-100-%28with-"pre-processing")\).

Other notes:  
\[3\] If it is already a palindrome, return whole string. \(For beating TLE on Leetcode.\)  
\[4\] Base case j=i=0: the max length of any palindromic substring from j to i is 1, as dp\[0\] itself forms a 1-length palindromic substring.  
\[5\] Copy previous row, for reference.  
\[6\] Base case j=i&gt;0: Same as j=i=0, dp\[j\] itself forms a 1-length palindromic substring.

```python
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if s == s[::-1]:  # [3]
            return len(s)
        S = len(s)
        dp = [0] * S
        dp[0] = 1  # [4]
        for i in range(1, S):
            prev = dp[:]  # [5]
            dp[i] = 1  # [6]
            for j in range(i-1, -1, -1):
                if s[i] == s[j]:  # [1]
                    dp[j] = 2 + prev[j+1]
                else:  # [2]
                    dp[j] = max(prev[j], dp[j+1])
        return dp[0]

```

