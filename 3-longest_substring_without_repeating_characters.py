class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        i = 0
        mp = {}
        
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]],i)
            
            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1
        return ans
'''
Time complexity : O(n). Index jj will iterate nn times.
Space complexity (HashMap) : O(min(m,n)). Same as the previous approach.
'''