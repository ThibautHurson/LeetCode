class Solution:
	def nextPermutation(self, nums):
		"""
		Do not return anything, modify nums in-place instead.
		"""
		n = len(nums) - 1
		k = n - 1
		for k in range(n - 1, -2, -1):
			if k >=0 and nums[k] < nums[k + 1]:
				i = k
				while i < n  and nums[k] < nums[i + 1]:
					i += 1

				nums[k], nums[i] = nums[i], nums[k]
				break
		
		for j in range(k + 1, k + 1 + (n + 1 - (k + 1))//2):
			nums[j], nums[n - (j - (k + 1))] = nums[n - (j - (k + 1))], nums[j]



'''
Time complexity: O(N) In worst case, only two scans of the whole array are needed.
Space complexity: O(1) In-place
'''

nums = [1, 2, 3]
sol = Solution()
sol.nextPermutation(nums)
print(nums)