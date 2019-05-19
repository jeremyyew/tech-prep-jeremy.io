'''

'''


class Solution:
    def numDecodings(self, s: str) -> int:
        def mergeCompatible(i: int) -> bool:
            if i < 0:
                return False
            return int(self.s[i:i+2]) <= 26
        S = len(s)
        if S <= 1:
            return S
        self.s = s
        dp = 1
        for i in range(1, S):
            if mergeCompatible(i-1):
                # print("i-1 true")
                if mergeCompatible(i-2):
                    # print("i-2 true")
                    dp *= 1.5
                else:
                    dp *= 2
            print(dp)
        return int(dp)
