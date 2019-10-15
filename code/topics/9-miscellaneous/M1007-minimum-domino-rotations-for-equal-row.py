'''
1. We start with the first domino, which gives us two candidate values `x` and `y` (the value that will fill one of the rows after flipping). 
2. For later dominoes, if they do not contain `x`, we can eliminate `x` as a candidate, same for `y`. 
3. At the end, if both have been eliminated, then there is no solution. 
4. Else, we might have one or two candidate values; just pick one and label `z`. 
5. The greater count of 'z' between `A` and `B` tells us that we should be flipping to replace the non-`z` elements in that array. That means the number of swaps is length - count. 

PS. length >= 2 so we can safely index 0 at the start.  
'''


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        x, y = A[0], B[0]  # [1]
        for i in range(1, len(A)):  # [2]
            if x not in (A[i], B[i]):
                x = None
            if y not in (A[i], B[i]):
                y = None
        if not x and not y:  # [3]
            return -1
        z = x or y  # [4]
        count_z = max(A.count(z), B.count(z))  # [5]
        return len(A) - count_z
