class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        UPPER_LIMIT = (2**31) - 1
        LOWER_LIMIT =  - 2**31
        sign = -1 if x < 0 else 1
        res = sign * int(str(abs(x))[::-1])
        return res if res <= UPPER_LIMIT and res >= LOWER_LIMIT else 0
        # Without using str:
        # 'pop' last digit n: get n with x % 10 and pop with x/= 10, push n onto rev with (rev * 10) + n
        # Check for overflow before pushing  
s = Solution().reverse(-987654)
print(s)