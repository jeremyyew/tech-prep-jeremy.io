'''
- **Brute force: O(N^2)**
    - Start with segment boundaries `l, r = 0, 1`.
    - Keep track of elements seen in dict. 
    - Check all elements on right, expand segment whenever a duplicate of a member of the current segment is seen. 
    - Start a new segment from `r + 1`, repeat. 
- **Expand right boundary based on last occurence: O(N)**
    - Get last occurences of all elements in dict. 
    - Set `r` as the last occurence of the first element. 
    - For every element, expand the right boundary if the last occurence of the current element is greater. 
        - i.e., if its last occurence is greater than the current `r`, update `r`. 
    - Elif we have reached `r`, then we have completed a segment, so reset and continue from `r + 1`. 
'''

class Solution(object):
    def partitionLabels(self, S):
        lastOcc = {}
        for i, n in enumerate(S):
            lastOcc[n] = i
        part_len, r, res = 0, None, []
        for i, n in enumerate(S):
            part_len += 1
            if not r: 
                r = lastOcc[n]
            if i == r: 
                res.append(part_len)
                part_len = 0
                r = None
            elif lastOcc[n] > r:
                r = lastOcc[n]
        return res
