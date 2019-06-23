# E13-roman-to-integer

* For each roman numeral, if the current value is less than the next numeral's value, we are at a 'boundary' number e.g. 4, 9, 40, 90, etc.
* If so, then instead of adding the value, we simply subtract that value.

```python
class Solution:
    def romanToInt(self, s) -> int:
        res = 0
        r_to_i = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        for i, n in enumerate(s):
            curr_val = r_to_i[n]
            if i == len(s) - 1:
                res += curr_val
                break
            next_val = r_to_i[s[i+1]]
            if curr_val >= next_val:
                res += curr_val
            else:
                res -= curr_val
        return res


# r = Solution().romanToInt('III')
# print(r)

# print(int(set(1)))

```

