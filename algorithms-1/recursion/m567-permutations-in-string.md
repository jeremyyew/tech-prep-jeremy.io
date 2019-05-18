# M567-permutations-in-string

```python
import itertools 

class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        d = {}
        for c in s1:
            if c in d: 
                d[c] += 1
            else: 
                d[c] = 1 
    
        start = 0
        end = len(s1) - 1
        while end < len(s2): 
            # print(s2[start:end + 1])
            temp = d.copy() # gotta reset, and use copy
            for i in range(end, start - 1, -1): # remember we end on start
                c = s2[i]
                # print(c)
                if c in temp and temp[c] > 0:
                    temp[c] -= 1
                    if i == start: # every e from end to start is a member of s1, no repeats, and we have len(s1) elements. so we have found a permutation.  
                        return True
                else: 
                    # shift past last found 'error'
                    start = i + 1
                    end = start + len(s1) - 1
                    break
        return False


# res = Solution().checkInclusion("ab", "eidbaooo")
# print(res)

```

