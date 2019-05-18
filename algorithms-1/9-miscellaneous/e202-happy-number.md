# E202-happy-number

```python
class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Let K be the first number, and P(K) be the magnitude of N. 
        # As N increases, P(K_N) will mostly decrease and stay within 0-200's range.  
        # Therefore it is a matter of time before it hits a repeated element. 
        self.seen = set()
        return self.traverse(n)
    def traverse(self, n): 
        # If seen before, we entered a loop
        if n in self.seen: 
            print(n, self.seen)
            return False
        # else, add to seen 
        self.seen.add(n)
        s = str(n)
        sumsq = 0
        for d in s: 
            sumsq = sumsq + int(d) ** 2
        if sumsq == 1: 
            return True
        return self.traverse(sumsq)
s = Solution()
print(s.isHappy(19))

```

