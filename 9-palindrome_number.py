import math
# Two pointers
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        left, right = 0, len(x) - 1
        
        while left < right:
            if x[left] != x[right]:
                return False
            left += 1
            right -= 1
        return True

'''
Time complexity: O(N) with N the number of digit
Time complexity: O(N)
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        if x // 10 == 0:
            return True
        exponent = math.floor(math.log10(x))

        while x != 0 and exponent > 0:
            power = 10**exponent

            if x % 10 != x // power:
                return False
            
            x = (x % power) // 10
            
            exponent -= 2
        return True

'''
Time complexity: O(N) with N the number of digit
Time complexity: O(1)
'''

x = 121
sol = Solution2().isPalindrome(x)
print(sol)