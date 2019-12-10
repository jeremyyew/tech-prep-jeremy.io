class Solution:
    def searchRange(self, nums, target):
        LEFT, RIGHT = 0, 1

        def bin_search_occ(l, r, direction):
            t = -1
            while l <= r:
                m = l + ((r-l) // 2)
                if target == nums[m]:
                    t = m
                    if direction == RIGHT:  # Look right.
                        l = m + 1
                    else:  # Look left.
                        r = m - 1
                elif target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            return t
        lo = bin_search_occ(0, len(nums)-1, LEFT)
        # Then we already know there are no values. Also, we can't use -1 for lo.
        if lo == -1:
            return [-1, -1]
        # Only look starting from lo.
        hi = bin_search_occ(lo, len(nums)-1, RIGHT)
        return [lo, hi]
