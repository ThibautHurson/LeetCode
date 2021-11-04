# Dynamic Programming
class Solution:
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for w in wordDict:
                if dp[i - len(w)] and s[i - len(w): i] == w:
                    dp[i] = True
        return dp[-1]
'''
d[i] is True if there is a word in the dictionary that ends at 
ith index of s AND d is also True at the 1st index (i.e d[0]=True)
'''

# s = 'catsandog'
# wordDict = ["cats","dog","sand","and","cat"]
s = "abcd"
wordDict = ["a","abc","b","cd"]
# s = "leetcode"
# wordDict = ["leet","code"]
sol = Solution()
print(sol.wordBreak(s, wordDict))

