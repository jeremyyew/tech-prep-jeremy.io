# E461-hamming-distance

```python
# Bitwise operators:
# & -> AND
# | -> OR
# ^ -> XOR
# ~ -> COMPLEMENT (flip bits)
# N << x -> LEFT SHIFT N by x bits


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return str(bin(x ^ y)).count('1')

```

