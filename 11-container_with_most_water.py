class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        if n < 2:
            return 0
        
        left = 0
        right = n-1
        res = 0
        while left < right:
            res = max(min(height[left], height[right]) * (right - left), res)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return res
'''
Time complexity : O(n). Single pass.
Space complexity : O(1). Constant space is used.
'''