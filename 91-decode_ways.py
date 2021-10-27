# Dynamic Programming with memory list 
class Solution:
    def numDecodings(self, s: str) -> int: 
        dp = [0 for x in range(len(s) + 1)] 

        # base case initialization
        dp[0] = 1 
        dp[1] = 0 if s[0] == "0" else 1   #(1)

        for i in range(2, len(s) + 1): 
            # One step jump
            if 0 < int(s[i-1:i]) <= 9:    #(2)
                dp[i] += dp[i - 1]
            # Two step jump
            if 10 <= int(s[i-2:i]) <= 26: #(3)
                dp[i] += dp[i - 2]
        return dp[len(s)]

'''
Time Complexity: O(N)
Space Complexity: O(N)
'''
# Same Approach without a memory list, just 3 variables
class Solution:
    def numDecodings(self, s: str) -> int:        
        past1 = 0 if s[0] == "0" else 1
        past2 = 1 
        
        if len(s) == 1:
            return past1
        
        for i in range(2, len(s) + 1):
            curr = 0
            # One step jump
            if 0 < int(s[i-1:i]) <= 9:    #(2)
                curr = past1
            # Two step jump
            if 10 <= int(s[i-2:i]) <= 26: #(3)
                curr += past2
            
            past2, past1 = past1, curr
        return curr

'''
Time Complexity: O(N)
Space Complexity: O(1)
'''