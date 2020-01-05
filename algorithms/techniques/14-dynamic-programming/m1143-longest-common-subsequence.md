# M1143-longest-common-subsequence

_Given two strings `text1` and `text2`, return the length of their longest common subsequence._

_A subsequence of a string is a new string generated from the original string with some characters\(can be none\) deleted without changing the relative order of the remaining characters. \(eg, "ace" is a subsequence of "abcde" while "aec" is not\). A common subsequence of two strings is a subsequence that is common to both strings._

_If there is no common subsequence, return 0._

```python
class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        I, J = len(t1), len(t2)
        dp = [[0 for _ in range(J+1)] for _ in range(I+1)]
        for i in range(1, I+1):
            for j in range(1, J+1):
                if t1[i-1] == t2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        for row in dp:
            print(row)
        return dp[I][J]


# Example: 'abcdefg', 'xcaebg'.
#    -  x  c  a  e  b  g
# - [0, 0, 0, 0, 0, 0, 0]
# a [0, 0, 0, 1, 1, 1, 1]
# b [0, 0, 0, 1, 1, 2, 2]
# c [0, 0, 1, 1, 1, 2, 2]
# d [0, 0, 1, 1, 1, 2, 2]
# e [0, 0, 1, 1, 2, 2, 2]
# f [0, 0, 1, 1, 2, 2, 2]
# g [0, 0, 1, 1, 2, 2, 3]

r = Solution().longestCommonSubsequence('abcdefg', 'xcaebg')
assert(r == 3)

# r = Solution().longestCommonSubsequence('', '')
# assert(r == 0)

# r = Solution().longestCommonSubsequence('', 'abcde')
# assert(r == 0)

# r = Solution().longestCommonSubsequence('abcde', '')
# assert(r == 0)

# r = Solution().longestCommonSubsequence('abcde', 'a')
# assert(r == 1)

# r = Solution().longestCommonSubsequence('abcde', 'xxxxaxxxxx')
# assert(r == 1)

# r = Solution().longestCommonSubsequence('abcde', 'abcde')
# assert(r == 5)

# r = Solution().longestCommonSubsequence('bsbininm', 'jmjkbkjkv')
# print(r)
# assert(r == 1)

```

