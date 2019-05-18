# M338-counting-bits

```python
'''
1. Brute force: 
    Count number of 1s in every number. 

2. Repeating sequence. 
    We may observe that the sequence of number of zeroes in binary numbers follows an increasing pattern that grows by the power 2: we copy the previous sequence plus 1, and append it to obtain the next sequence to copy. 

    [0]
    [0] + [0+1]
    [0, 1] + [0+1, 1+1]
    [0, 1, 1, 2] + [0+1, 1+1, 1+1, 2+1]
    ...

    Instead of counting where we are in the sequence and terminating at the appropriate time, we may instead define a function for every index that gives us the correct index to look back at. 
        
    [1] The powers of 2 are the start of each repeating sequence. So, get m, the maximum power of 2 that is less than or equals to n. 
    [2] We look back on num_bits[n-m], as n-m is the offset of n from the closest power of 2.
    [3] Base case n=0: We cannot log 0, so make sure we never do it. We can start with 0-filled array, or we can have a base case. 
    [4] Remember they are asking for 0 to n, not 0 to n-1!!
    [5] We obtain the max power of 2 less than or equal to n by rounding logn, and using that as power of 2. 
'''
import math


class Solution:
    def countBits(self, num: int) -> List[int]:
        num_bits = [0 for _ in range(num+1)]  # [4]
        for n in range(1, num+1):  # [3]
            m = self.max_power_two(n)  # [1]
            num_bits[n] = num_bits[n-m] + 1  # [2]
        return num_bits

    def max_power_two(self, n):
        return 2 ** int(math.log(n, 2))  # [5]

```

