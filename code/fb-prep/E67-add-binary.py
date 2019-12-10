class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b, 2)))[2:]


r = Solution().addBinary('11', '1')
print(r)
