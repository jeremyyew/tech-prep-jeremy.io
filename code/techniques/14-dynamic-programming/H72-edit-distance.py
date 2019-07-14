'''
Bottom up, O(1) space solution is mine. For the rest of the approaches (and explanation) see https://leetcode.com/problems/edit-distance/discuss/159295/Python-solutions-and-intuition.
'''


class Solution:
    def minDistance(self, word1, word2):
        M = len(word1)
        N = len(word2)
        prev = list(range(N+1))
        curr = [None] * (N+1)
        for m in range(1, M + 1):
            curr[0] = m
            for n in range(1, N + 1):
                if word1[m-1] == word2[n-1]:
                    curr[n] = prev[n-1]  # Matching, no edit.
                else:
                    curr[n] = 1 + min(prev[n],  # Delete nth char in word2.
                                      # Insert mth char in word1.
                                      curr[n-1],
                                      prev[n-1])  # Replace either.
            prev = curr.copy()
        return prev[-1]


class SolutionGrid:
    def minDistance(self, word1, word2):
        M = len(word1)
        N = len(word2)
        dp = [[0] * (N + 1) for _ in range(M + 1)]
        # Initialize base cases.
        for m in range(M + 1):
            dp[m][0] = m
        for n in range(N + 1):
            dp[0][n] = n
        # Iterative bottom up.
        for m in range(1, M + 1):
            for n in range(1, N + 1):
                if word1[m-1] == word2[n-1]:
                    dp[m][n] = dp[m-1][n-1]  # Matching, no edit.
                else:
                    dp[m][n] = 1 + min(dp[m-1][n],  # Delete nth char in word2.
                                       dp[m][n-1],  # Insert mth char in word1.
                                       dp[m-1][n-1]  # Replace either.
                                       )
        return dp[-1][-1]


class SolutionRec:
    def minDistance(self, word1, word2):
        if not word1 and not word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        insert = 1 + self.minDistance(word1, word2[1:])
        delete = 1 + self.minDistance(word1[1:], word2)
        replace = 1 + self.minDistance(word1[1:], word2[1:])
        return min(insert, replace, delete)
