class Solution:
	def jump(self, nums):
		if len(nums) <= 1:
			return 0
		jumps = 1 
		start = 0
		while start + nums[start] < len(nums) - 1:
			for k in range(start+1, start + 1 + nums[start]):
				if nums[k-1] - 1 > nums[k]:
					nums[k] = nums[k - 1] - 1
			start += nums[start]
			jumps += 1

		return jumps

nums = [1]
sol = Solution()
print(sol.jump(nums))

'''
Time complexity : O(N)

Space complexity : O(1)
'''