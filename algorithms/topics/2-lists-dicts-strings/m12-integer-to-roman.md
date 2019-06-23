# M12-integer-to-roman

* We can parse the digits from left to right or right to left. Here we parse in reverse so we can conveniently use the index as the power, instead of keeping track of the current power in a variable. 
* We simply need to **partition the range of digits** **into 5 cases**: 0-3, 4, 5, 6-8, and 9. Then we index into our keys with the digit modified by the power \(e.g. 10^i, ****10^i \* 5\) to get the appropriate character. 

```python

class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        keys = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }
        digits = str(num)[::-1]
        for i, d in enumerate(digits):
            d = int(d)
            if d < 4:
                add = keys[10**i] * d
            elif d == 4:
                add = keys[10**i] + keys[10**i * 5]
            elif d == 5:
                add = keys[10**i * 5]
            elif d > 5 and d < 9:
                add = keys[10**i * 5] + keys[10**i] * (d-5)
            else:
                add = keys[10**i] + keys[10**(i + 1)]
            roman = add + roman
            # print(f'add={add}, roman={roman}, i={i}, d={d}')
        return roman



```

