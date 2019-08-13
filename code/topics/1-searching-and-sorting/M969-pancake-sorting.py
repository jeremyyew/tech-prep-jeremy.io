'''
- To sort: O(N) flips. 
    - Bring max to front, and flip it to the back. Repeat but excluding that element. 
- To get next max index: O(N^2) 
    - Save indexes of sorted list initially, and for each next biggest number update its index based on all previous flips.
    - Save indexes of sorted list initially, and update all affected indexes based on last two flips. Then get the next biggest. 
    - Actually reverse the list, and traverse to get the next max index. 
'''


class Solution(object):
    def pancakeSort(self, A):
        def getMaxIndex(nums):
            # Returns first occurence, but that's ok.
            return nums.index(max(nums))
        ans = []
        while len(A) > 1:
            print(A)
            i = getMaxIndex(A)
            A[:i+1] = reversed(A[:i+1])
            A = list(reversed(A))
            ans.extend([i+1, len(A)])
            A = A[:-1]
        return ans


# r = Solution().pancakeSort([3, 2, 4, 1])
# print(r)
