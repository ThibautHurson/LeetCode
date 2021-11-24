# Approach 1: Brute Force
class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        return sum(self.numTrees(i - 1) * self.numTrees(n - i) for i in range(1, n+1))

'''
Time complexity: O(3**N) where N is the given number of nodes in BST
Space complexity: O(N) the maximum recursive stack depth.
'''


# Approach 2: Dynamic Programming
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]

'''
Time Complexity : O(N2), we iterate over the range i=[2, n] and iteratively calculate dp[i]. 
            The total number of operations performed equals 2+3+4+5..n = (n*(n+1)/2)-1 ≈ O(N2)
Space Complexity : O(N), required to store the results in dp
'''