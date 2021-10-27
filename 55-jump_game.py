# Backward, one pass
class Solution:
    def canJump(self, nums):
        last = len(nums) - 1

        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= last:
                last = i
        return last == 0

# Forward, one pass
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False

        jumps = nums[0]
        for k in range(len(nums)):
            jumps = max(jumps - 1, nums[k])
            if jumps == 0 and k != len(nums) - 1:
                return False
            if k + jumps >= len(nums) - 1:
                return True

'''
Time Complexity: O(N)
Space Complexity: O(1)
'''