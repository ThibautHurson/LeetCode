#Approach: Expand Around Center

class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.min_idx, self.max_idx = 0, 0
        self.length = len(s)
        
        for i in range(self.length):
            self.helper(s, i, i)
            self.helper(s, i, i + 1)
         
        return s[self.min_idx: self.max_idx+1]
               
    def helper(self, s, i , j):
        while i >= 0 and j < self.length and s[i] == s[j]:
            i -= 1
            j += 1
        i, j = i+1, j-1
        if j - i > self.max_idx - self.min_idx:
            self.min_idx, self.max_idx = i, j

'''
Time complexity : O(n^2) Since expanding a palindrome around its center could take O(n) time,
 the overall complexity is O(n^2).

Space complexity : O(1)
'''