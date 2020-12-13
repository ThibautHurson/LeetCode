#Approach 2: set
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        unique_nb = set()
        for val in nums:
            if val in unique_nb:
                return val
            else:
                unique_nb.add(val)
'''
Time complexity : O(n)
Space complexity : O(n)
'''
#Approach 1: sort
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]
'''
Time complexity : O(nlgn)
Space complexity : O(1)
'''
#Approach 3: Floyd's Tortoise and Hare (Cycle Detection)
class Solution:
    def findDuplicate(self, nums):
        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare
'''
Time complexity : O(n)
Space complexity : O(1)
'''