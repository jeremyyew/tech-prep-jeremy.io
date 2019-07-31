# E20-valid-parenthesis

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stk, mapping = [], {'(': ')', '[': ']', '{': '}'},
        for c in s:
            if c in ('(', '{', '['):
                stk.append(c)
            else:
                if not stk or mapping[stk.pop()] != c:
                    return False
        return (not stk)

```

