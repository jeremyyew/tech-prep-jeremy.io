# E53-maximum-subarray

```python
from typing import List, Tuple

''' 
    DP, iterative and linear. 
        Let OPT_WITH be the maximum sum of a contiguous subarray that ends in nums[i]. Then when computing the next OPT_WITH we are deciding whether to include "baggage" of previous contiguous values or start afresh with i: 

        OPT_WITH(i) = max(nums[i], 
                          nums[i] + OPT_WITH(i-1))

        Let OPT_SUM be the maximum sum of any contiguous subarray within 0 to i. Then when computing the next OPT_SUM we are checking if we have we beaten our previous optimal: 

        OPT_SUM(i) = max(OPT_SUM(i-1),
                         OPT_WITH(i))
        '''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 
        maxSum =currentSum = nums[0]
        for num in nums[1:]:
            currentSum = max(currentSum+num, num)
            maxSum = max(currentSum, maxSum)
        return maxSum


class SolutionDP:
    def maxSubArray(self, nums: List[int]) -> int:
        OPT_WITH = None
        OPT_SUM = None
        for i in range(len(nums)):
            # print(OPT_RE[i], nums[i])
            if i == 0:
                OPT_WITH = nums[i]
                OPT_SUM = nums[i]
                continue
            OPT_WITH = max(nums[i], nums[i] + OPT_WITH)
            OPT_SUM = max(OPT_WITH, OPT_SUM)
        return OPT_SUM


# print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

# Takes too long.
# Try:
# - returning results rather than shared memory.
# - build matrix iteratively rather than recursive calls

'''
    DP, divide and conquer. 

    Let OPT(s, e) be the max sum of all contiguous subarrays within start index s to end index e. 
    Let OPT_RE(s,e) be the max sum of all contiguous subarrays within start index s to end index e that contains the element at e, i.e. the right edge. 
    OPT_LE(s,e) is the same but containing the element at s, i.e. the left edge. 
    Let OPT_T be the max sum of the entire subarray from s to e. We will need this in computing the new OPT_RE and OPT_LE of two merged subarrays. 

    BASE CASE: 
        if s == e:  
            OPT(s, e) = nums[s]
            OPT_LE(s, e) = nums[s]
            OPT_RE(s, e) = nums[s]
            OPT_T(s, e) = nums[s]

    INDUCTION CASE:                
        (where m = (s + e) // 2)
        OPT(s, e) = max(OPT(s, m),
                        OPT(m+1, e), 
                        OPT_RE(s, m) + OPT_LE(m+1, e))
        OPT_LE(s, e) = max(OPT_LE(s, m), 
                          OPT_LE(m+1, e) + OPT_T(s, m))
        OPT_RE(s, e) = max(OPT_RE(m+1, e), 
                           OPT_RE(s, m) + OPT_T(m+1, e))
        OPT_T(s, e) = OPT_T(s, m) + OPT_T(m+1, e)

    Notes:
    - A previous solution wrote previously computed results to a shared memory matrix (O(N^2) space) in order to avoid passing too many parameters around (and making it easier to declare required data).
    - However, it ended up taking too long for large N (~10K). 
    - Hypothesis was that reading/writing from shared memory takes longer than passing parameters. Seems to be true.
    - Here we use no shared memory except nums array, which is only accessed in the base case.
    '''


class SolutionDNC:
    def maxSubArray(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        self.nums = nums
        OPT, _, _, _ = self.split_then_merge(
            start, end)
        return OPT

    def split_then_merge(self, s: int, e: int) -> (int, int, int, int):
        if s == e:
            return self.nums[s], self.nums[s], self.nums[s], self.nums[s]
        else:
            m = (s + e) // 2
            OPT_L, OPT_L_LE, OPT_L_RE, OPT_L_T = self.split_then_merge(
                s, m)
            OPT_R, OPT_R_LE, OPT_R_RE, OPT_R_T = self.split_then_merge(
                m+1, e)
            OPT = max(OPT_L,
                      OPT_R,
                      OPT_L_RE + OPT_R_LE)
            OPT_LE = max(OPT_L_LE,
                         OPT_L_T + OPT_R_LE)
            OPT_RE = max(OPT_R_RE,
                         OPT_R_T + OPT_L_RE)
            OPT_T = OPT_L_T + OPT_R_T
        return OPT, OPT_LE, OPT_RE, OPT_T

# print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# assert(SolutionDC().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6)

```

