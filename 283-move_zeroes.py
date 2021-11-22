class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for k in range(len(nums)):
            if nums[k] == 0:
                count += 1
            elif nums[k] != 0 and count != 0:
                nums[k - count], nums[k] = nums[k], nums[k - count]

'''
Time complexity : O(N)
Space complexity : O(1)
'''

