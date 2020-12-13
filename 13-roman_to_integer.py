class Solution:
    def romanToInt(self, s: str) -> int:
        
        numeral = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        exception = {'IV': 4,'IX': 9,'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        res = 0
        k = 0
        n = len(s)
        while k < n - 1:
            if s[k:k+2] in exception:
                res += exception[s[k:k+2]]
                k += 2
            else:
                res += numeral[s[k]]
                k += 1
        if k == n - 1: res += numeral[s[k]]
            
        return res

'''
temp: O(n)
spat: O(1)
'''