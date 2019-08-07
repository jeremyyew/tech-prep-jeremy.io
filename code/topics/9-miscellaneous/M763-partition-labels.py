class Solution(object):
    def partitionLabels(self, S):
        lastOcc = {}
        res = []
        for i, n in enumerate(S):
            lastOcc[n] = i
        part_len, r = 0, None
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
