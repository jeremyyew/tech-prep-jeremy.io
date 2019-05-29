# M287-find-duplicate-number

1. **Collect with set**: O\(N\) time, O\(N\) space
2. **Sort then scan**: O\(NlogN\) time, O\(N\) or O\(1\) space
3. **Cyclic Sort**: O\(N\) time, O\(1\) space \(modify input array\) \(Submitted\)
   * Cyclic sort until we enter the cycle \(see the same value\).
   * We write each value to its exact index \(as opposed to i+1 such as in E268 Missing Number\) starting from 0. Since there is no zero value, we will be constantly shifting values from the first step until we hit a duplicate.  
   * The commented out line can replace the three lines in the loop. It's really pretty but tricky: even though the order of getting values on the RHS doesn't matter, on the LHS you MUST assign `nums[i]` first before `i` \(left-to-right\), since we want to assign to the old `i` position before changing `i`. 
4. **Detect Cycle**: O\(N\) time, O\(1\) space 
   * Treat the array slots as linked list nodes whose values point to indices of the array.
   * Since all values are between 1 to n, we can never go out of bounds, so the path starting from index 0 will go on infinitely, i.e. it contains a cycle.
   * However, the entire path cannot be a cycle, since we start from index 0.
   * Therefore, the start of the cycle will have two distinct pointers pointing to it, and these are by definition a pair of duplicate values.
   * The distance `d` between these two points is equal to the length of the cycle, since that is the distance traversed from when we enter the cycle to when we reach the start of the cycle again.
   * Using the Fast/Slow pointer technique, we find the point where the two pointers meet. The distance from the start to the meeting point is equal to the length of the cycle. For explanation, see [https://leetcode.com/problems/linked-list-cycle-ii/](https://leetcode.com/problems/linked-list-cycle-ii/)
   * From here, simply traverse two pointers at the same speed, one from 0 and one from `d`; we will eventually hit the two equal-value pointers.

```python
class Solution:
    def findDuplicate(self, nums):
        i = 0
        while i != nums[i]:
            k = nums[i]
            nums[i] = i
            i = k
            # [1]: nums[i], i = i, nums[i]
        return i


class SolutionDetectCycle:
    def findDuplicate(self, nums):
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        p1, p2 = nums[0], slow
        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]
        return p1

```

