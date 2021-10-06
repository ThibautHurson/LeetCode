# Approach 1: int -> str -> int conversion
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        rev = sign * int(str(abs(x))[::-1])
        
        return rev if (rev >= -2**31 and rev <= 2**31 - 1) else 0

'''
Time Complexity: O(log(x)). There are roughly log_{10}(x) digits in x.
Space Complexity: O(log(x)).
'''

# Approach 2: Pop and Push Digits & Check before Overflow
class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)
        max_int = 2**31
        
        while x != 0:
            pop = x % 10
            x = int(x / 10)
            
            if rev > max_int / 10 or (rev == max_int / 10 and pop > 7):
                return 0
            
            rev = rev * 10 + pop
        return sign*rev

'''
Time Complexity: O(log(x)). There are roughly log_{10}(x) digits in x.
Space Complexity: O(1).
'''