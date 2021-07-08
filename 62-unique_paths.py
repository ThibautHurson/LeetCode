# Approach 1: Combinatorial problem
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # have to go m - 1 down, and n - 1 right. It is a combinatorial problem.
        # At each step you go either rigth or down. Therefore we can see the problem as the one
        # of choosing m - 1 steps in which you go down among (m - 1) + (n - 1) = (m + n - 2) steps.
        # That is C(m + n - 2, m - 1).
        
        return int(math.factorial(m + n - 2)/math.factorial(m - 1)/math.factorial(n - 1))

# Approach 2: Dynamic programming
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        count = [[1 for i in range(m)] for j in range(n)]
        
        for i in range(1,m-1):
            for j in range(1,n-1):
                # count the number of ways to arrive at (i, j)
                count[i][j] = count[i-1][j] + count[i][j-1]
        return count[-1][-1]

# Even less redundant
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j - 1] + dp[j]
        return dp[-1] if m and n else 0