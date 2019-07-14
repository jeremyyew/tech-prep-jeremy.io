''' 
dp[i,j] = if s3[i+j] not in (s1[i], s2[i]) then False
                else if i >= 0 and s3[i+j] == s1[i] and dp[i-1,j]) 
                     OR 
                     if j >= 0 and s3[i+j] == s2[j] and dp[i,j-1])
'''


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        I, J, K = len(s1), len(s2), len(s3)
        if I + J != K:
            return False
        curr = [False for _ in range(J + 1)]
        for i in range(I+1):
            prev = curr.copy()
            for j in range(J+1):
                if i == 0 and j == 0:
                    curr[j] = True
                else:
                    curr[j] = \
                        (i > 0 and s3[(i+j)-1] == s1[i-1] and prev[j]) or \
                        (j > 0 and s3[(i+j)-1] == s2[j-1] and curr[j-1])
        return curr[-1]


class SolutionGrid:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        I, J, K = len(s1), len(s2), len(s3)
        if I + J != K:
            return False
        dp = [[False for _ in range(J + 1)] for _ in range(I + 1)]
        for i in range(I+1):
            for j in range(J+1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                else:
                    dp[i][j] = \
                        (i > 0 and s3[(i+j)-1] == s1[i-1] and dp[i-1][j]) or \
                        (j > 0 and s3[(i+j)-1] == s2[j-1] and dp[i][j-1])
        return dp[-1][-1]

# r = Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac")
# print(r)


class SolutionRec:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3
        if not s3:
            return (not s1 and not s2)
        pick1 = pick2 = False
        if s3[0] == s1[0]:
            pick1 = self.isInterleave(s1[1:], s2, s3[1:])
        if s3[0] == s2[0]:
            pick2 = self.isInterleave(s1, s2[1:], s3[1:])
        return pick1 or pick2
