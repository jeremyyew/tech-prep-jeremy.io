'''
Note: initially I used a dict with last_value:length key pairs, but its much cleaner to just use a list to store lengths, and accessing last values by indexing nums. 

- For each subseqence ending in the i-th element, we obtain its max length by finding the max length of all previous subsequences that end in some j-th element nums[j] that is less than nums[i] (where j < i), and then we add one. 

More formally: 
    lengths[i] = max{lengths[j] where 0 < j < i and nums[j] < nums[i]} + 1

- We could then compare lengths[i] with the max length so far to see if it is the new longest subsequence length. However in this implementation, we only find the max at the end since we don't really need it intermediately. 

- Even if lengths[i] isn't a new max, we still need to save it, since it may end up being part of a new max later on. 
'''


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        lengths = [None for _ in range(len(nums))]
        lengths[0] = 1
        for i in range(1, len(nums)):
            subseq_i_len = max([lengths[j]
                                for j in range(i) if nums[j] < nums[i]] or [0]) + 1
            lengths[i] = subseq_i_len
        return max(lengths)


class SolutionDict:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        subseq = {nums[0]: 1}
        for i in range(1, len(nums)):
            subseq_i_len = max(
                [length if j < nums[i] else 0 for j, length in subseq.items()]) + 1
            subseq[nums[i]] = subseq_i_len
        return max(subseq.values())
