class Solution(object):
    def getMedian(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0], 0
        elif n == 2:
            return (nums[0] + nums[1]) / 2, 1
        elif n % 2 == 1:
            return nums[n//2 + 1], n/2
        else:
            return (nums[n//2] + nums[n//2 + 1]) / 2, n//2

    def baseCase(self, nums1, nums2):
        if not nums1 and not nums2:
            raise ValueError
        if not nums1:
            return nums2[0]
        if not nums2:
            return nums1[0]
        if len(nums1) == 1 and len(nums2) == 1:
            print((nums1[0] + nums2[0]) / 2)
            return (nums1[0] + nums2[0]) / 2
        if len(nums2) == 1:  # swap
            temp = nums1
            nums1 = nums2
            nums2 = temp

        med, i = self.getMedian(nums2)
        # print(med, i)
        n2 = len(nums2)
        if med == nums1[0]:
            return nums1[0]
        elif n2 % 2 == 0:
            if med > nums1[0]:
                n2th = nums2[n2//2 - 1]
                if nums1[0] <= n2th:
                    return nums1[0]
                else:
                    return n2th
            else:
                n2th = nums2[n2//2]
                if nums1[0] >= n2th:
                    return n2th
                else:
                    return nums1[0]
        else:
            if med > nums1[0]:
                n2th = nums2[n2//2 - 1]
                if nums1[0] > n2th:
                    return (nums1[0] + med) / 2
                else:
                    return (n2th + med) / 2
            else:
                n2th = nums2[n2//2 + 1]
                if nums1[0] < n2th:
                    return (nums1[0] + med) / 2
                else:
                    return (n2th + med) / 2

    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) <= 1 or len(nums2) <= 1:
            return self.baseCase(nums1, nums2)

        n1_med, n1_med_i = self.getMedian(nums1)
        n2_med, n2_med_i = self.getMedian(nums2)

        if n1_med == n2_med:
            return n1_med
        elif n1_med > n2_med:
            bigger, bigger_i, smaller, smaller_i = nums1, n1_med_i, nums2, n2_med_i
        else:
            bigger, bigger_i, smaller, smaller_i = nums2, n2_med_i, nums1, n1_med_i
        nums1 = bigger[0:bigger_i]
        nums2 = smaller[smaller_i:len(nums2)]
        return self.findMedianSortedArrays(nums1, nums2)


# print(Solution().findMedianSortedArrays([], [1]))
# print(Solution().findMedianSortedArrays([1,3], [2]))

print(Solution().findMedianSortedArrays([1, 2], [3, 4]))
