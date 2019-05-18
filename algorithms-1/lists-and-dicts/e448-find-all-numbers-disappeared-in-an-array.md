# E448-find-all-numbers-disappeared-in-an-array

* This solution uses no extra space: write each value in its index, essentially using the array as a dict.
* It's a bit slower since we might traverse an element multiple times. But its linear - in this case, each index is traversed at most four times since each element appears at most twice, so 2 x 'jumps' to i, 1 possible traversal via outer loop, and 1 final traversal to collect missing values.
* Even if there is no limit on number of times an element appears, the worst case is 2n jumps. In the worst case, all n indices have a displaced value, so all jump at least once. However, each sequence of k jumps in the inner loop assigns k indices their proper value, and these indices can no longer be jumped from. So the total number of additional jumps is n.
* The faster way would be to use a separate array, or perhaps a bitmap. That would get us 2n time and O\(n\) space \(with a bitmap, its n bits which means O\(1\) if n &lt; num of bits representing one integer element\).

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # def check(i):
        #     if i < 1 or i > n:
        #         raise ValueError

        i = 1
        n = len(nums)
        while i < n + 1:
            if nums[i-1] == i:
                pass
            else:
                k = nums[i-1]
                # check(k)
                while k != nums[k-1]:
                    j = nums[k-1]
                    # check(j)
                    nums[k-1] = k
                    k = j
            i += 1
        disappeared = []
        for m in range(1, n+1):
            if nums[m-1] != m:
                disappeared.append(m)
        return disappeared

# This one is elegant and O(n) space and time.


class SolutionFast:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums) + 1)) - set(nums))

```

