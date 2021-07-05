# Approach 1: Recursion
class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (first_match and self.isMatch(text[1:], pattern)) or \
                    self.isMatch(text, pattern[2:])
            #1st part: the first letter matches the pattern and we have * after it.
            #then we need to look at text's next letter to see if letter* still deals with it
            #2nd part: If we have a match on the remaining strings after any of these operations, 
            #then the initial inputs matched.
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])


'''
For time and space complexity:
https://leetcode.com/problems/regular-expression-matching/solution/
for both: O( (T+P)2**(T+P/2))
'''

# Approach 2: Dynamic Programming
# Top-Down Variation
class Solution(object):
    def isMatch(self, text, pattern):
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)

# Bottom-Up Variation
class Solution(object):
    def isMatch(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]

'''
Time Complexity: Let T, PT,P be the lengths of the text and the pattern respectively. 
The work for every call to dp(i, j) for i=0, ... ,Ti=0,...,T; j=0, ... ,Pj=0,...,P is done once, 
and it is O(1)O(1) work. Hence, the time complexity is O(TP)O(TP).

Space Complexity: The only memory we use is the O(TP)O(TP) boolean entries in our cache. 
Hence, the space complexity is O(TP)O(TP).
'''
