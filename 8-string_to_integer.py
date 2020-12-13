class Solution:
    def myAtoi(self, s: str) -> int:
        
        have_num = False
        if not s:
            return 0
        idx = 0
        n = len(s)
        res = 0
        
        while idx < n:
            if s[idx] == ' ':
                idx += 1
                continue
            if s[idx] != '-' and s[idx] != '+' and (not s[idx].isnumeric()):
                return 0
            if s[idx].isnumeric():
                have_num = True
                break
            if s[idx] == '-' or s[idx] == '+':
                if idx < n-1 and s[idx+1].isnumeric():
                    have_num = True
                    idx += 1
                    break
                else:
                    return 0
            
        if not have_num:
            return 0
        
        if s[max(idx-1,0)] == '-':
            sign = -1
        else:
            sign = +1
        
        start = idx
        while idx < n and s[idx].isnumeric() :
            idx += 1
        
        max_value = 2**31 
        res = sign*int(s[start:idx])
        if res > max_value - 1 :
            return max_value -1
        if res < -max_value:
            return -max_value
        
        return res
'''
Time Complexity: O(N). Here, N is the length of string str. We perform only one iteration over string str.
Space Complexity: O(1) We use constant extra space for storing sign of the result.
'''