# M647-palindromic-substrings

```python
class Solution(object):
    def countSubstrings(self, S):
        N = len(S)
        ans = 0
        for i in range(2*N - 1):
            l = i // 2
            r = l + (i // 2)
            while l >= 0 and r < N and S[l] == S[r]:
                ans += 1
                l -= 1
                r += 1
        return ans
```

