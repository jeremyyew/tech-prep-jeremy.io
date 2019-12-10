class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        l, r = 0, len(height) - 1
        while l < r:
            width = r - l
            if height[l] > height[r]:
                area = height[r] * width
                r -= 1
            else:
                area = height[l] * width
                l += 1
            maxArea = max(area, maxArea)
        return maxArea
