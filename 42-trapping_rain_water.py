#Solution using two pointers
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        water = 0
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        
        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                water += left_max - height[left]
                left += 1
                
            else:
                right_max = max(right_max, height[right])
                water += right_max - height[right]
                right -= 1
        return water
'''
Time complexity: O(n). Single iteration of O(n).
Space complexity: O(1) extra space. Only constant space required for left, right, 
left_max and right_max.
'''