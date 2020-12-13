class Solution:
    def longestPalindrome(self, s):
        res = ""
        self.length = len(s)
        
        for i in range (self.length):
            tmp = self.helper(s,i,i)
            if len(tmp)> len(res):
                res = tmp

            tmp = self.helper(s,i,i+1)
            if len(tmp)> len(res):
                res = tmp
        
        return res
    
    def helper(self,s,i,j):
        
        while i >= 0 and j < self.length and s[i]==s[j]:
            i -= 1
            j += 1
        
        return s[i+1:j] 