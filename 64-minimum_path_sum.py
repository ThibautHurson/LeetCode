# Approach 1: Dynamic Programming: using the input grid
class Solution:
	def minPathSum(self, grid):
		m, n = len(grid), len(grid[0])

		for j in range(0, n):
			for i in range(0, m):
				if i == 0 and j != 0:
					grid[i][j] += grid[i][j-1]
				elif i != 0 and j == 0:
					grid[i][j] += grid[i-1][j]
				elif i != 0 and j != 0:
					grid[i][j] += min(grid[i-1][j], grid[i][j-1])
								
		return grid[m-1][n-1]

grid = [[1,3,1],[1,5,1],[4,2,1]]

'''
Note: If needed a memo grid could be used to keep grid unchanged

Time complexity : O(m*n)
Space complexity : O(1) or O(m*n) with a memo grid
'''


# Approach 1: Dynamic Programming: using a memo vector of size (1, N)
class Solution:
	def minPathSum(self, grid):
	        M, N = len(grid), len(grid[0]) 
	        dp = [0] + [float('inf')] * (N-1)
	        for i in range(M):
	            dp[0] = dp[0] + grid[i][0]
	            for j in range(1, N):
	                dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
	        return dp[-1]


'''
Time complexity : O(N)

Space complexity : O(1)
'''


sol = Solution()
print(sol.minPathSum(grid))


