class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        letter_count = {}
        for l in range (len(s)):
            if s[l] not in letter_count:
                letter_count[s[l]] = 1
            else:
                letter_count[s[l]] += 1
            
            if t[l] not in letter_count:
                letter_count[t[l]] = -1
            else:
                letter_count[t[l]] -= 1
                
        for v in letter_count.values():
            if v!=0:
                return False
        return True
'''            
Complexity analysis

Time complexity : O(n). Time complexity is O(n) because accessing the counter table is a constant time operation.

Space complexity : O(1). Although we do use extra space, the space complexity is O(1) because the table's size stays constant no matter how large n is.
Follow up question:
Use a hash table instead of a fixed size counter. Imagine allocating a large size array to fit the entire range of unicode characters, which could go up 
to more than 1 million. A hash table is a more generic solution and could adapt to any range of characters.
'''