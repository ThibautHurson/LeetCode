class Solution:
    def maxProfit(self, prices):
        profit = 0
        curr_min = prices[0]
        for i in range(1, len(prices)):
            if prices[i] == curr_min:
                continue
            elif prices[i] > curr_min:
                profit += prices[i] - curr_min
                curr_min = prices[i]
            elif prices[i] < curr_min:
                curr_min = prices[i]
        return profit

'''
Time complexity: O(N)
Space complexity: O(1)
'''

prices = [7,10,6,7]
sol = Solution()
print(sol.maxProfit(prices))
