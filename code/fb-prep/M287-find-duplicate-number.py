class Solution:
    def findDuplicate(self, nums):
        i = 0
        while i != nums[i]:
            print(i)
            k = nums[i]
            nums[i] = i
            i = k
            # [1]: nums[i], i = i, nums[i]
            print(nums)
        return i


r = Solution().findDuplicate([1, 1, 2, 3, 4])
print(r)
r = Solution().findDuplicate([1, 3, 4, 2, 2])
print(r)


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


class SolutionDetectCycleAlt:
    def findDuplicate(self, nums):
        slow = fast = 0
        while not (nums[slow] == nums[fast] and slow != fast):
            print(slow, fast)
            slow = nums[slow]
            fast = nums[fast]
            if nums[slow] == nums[fast]:
                break
            fast = nums[fast]
        return nums[slow]
