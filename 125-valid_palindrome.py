class Solution:
    def isPalindrome(self, s: str) -> bool:
        min = 0
        max = len(s)-1
        
        while min < max:
            if not s[min].isalnum():
                min += 1
            elif not s[max].isalnum():
                max -= 1
            else:
                if s[min].lower() != s[max].lower():
                    return False
                else:
                    min +=1
                    max -= 1
        return True
