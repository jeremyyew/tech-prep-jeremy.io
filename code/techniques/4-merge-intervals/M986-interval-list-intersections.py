'''
Cases:  
1. No `intersection(a, b)`:  
    1. `a[1] < b[1]`: `a` has no intersections with the rest of `B`, go to next `a`.  
    2. `a[1] > b[1]`: `b` has no intersections with the rest of `A`, go to next `b`.  
    3. `a[1] == b[1]`: Neither `a` or `b` have any more intersections, go to next `a` AND next `b`.  
2. `intersection(a, b)`:  
    1. Register the current intersection (merging with previously added intersections if necessary). Then apply same rules as 1.1-1.3.  
    3. Note: does not assume `A` and `B` are same length. Once one runs out, there are no more intersections.  
    4. You don't actually have to take into account case 1.3. Going only into the next `b` for example will just bring us into case 1.1 (at the negligible cost of one additional iteration).  
'''
from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        def intersection(a, b) -> List[int]:
            if a[1] < b[0] or a[0] > b[1]:
                return None
            return [max(a[0], b[0]), min(a[1], b[1])]
        i, j, merged = 0, 0, []
        while i < len(A) and j < len(B):  # [3]
            a, b = A[i], B[j]
            ab = intersection(a, b)
            if ab:  # [2]
                if merged and intersection(merged[-1], ab):
                    merged[-1] = intersection(merged[-1], ab)
                else:
                    merged.append(ab)
            # [1], [4]
            if a[1] < b[1]:
                i += 1
            else:
                j += 1
        return merged
