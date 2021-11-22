# Approach 1: Using a set
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        unique = set(nums)
        res = []
        for k in range(1, len(nums) + 1):
            if k not in unique:
                res.append(k)
        return res

'''
Time complexity: O(N)
Space complexity: O(N)
'''

# Approach 2: O(1) space
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]

'''
Time complexity: O(N)
Space complexity: O(1)
'''


nums = [4,3,2,7,8,2,3,1]
sol = Solution()
print(sol.findDisappearedNumbers(nums))