# E189-rotate-array

* Challenge is to be in place, O\(1\) space. Otherwise just concatenate and reassign. 
* Can either reverse multiple times, or cyclic replace \(must write your own in-place reverse, for some reason Python's reverse is supposed to be in-place but doesn't work\). 

```python
class Solution:
    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k = k % N
        count = 0
        for start_i in range(N):
            current_i = start_i
            prev = nums[start_i]
            while count < N:
                next_i = (current_i + k) % N
                temp = nums[next_i]
                nums[next_i] = prev
                prev = temp
                current_i = next_i
                count += 1
                if start_i == current_i:
                    break
        print(nums)


Solution().rotate([1, 2, 3, 4, 5, 6], 2)
Solution().rotate([1, 2, 3, 4, 5, 6], 3)

```

