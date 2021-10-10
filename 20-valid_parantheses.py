# Using a stack
class Solution:
    def isValid(self, s: str) -> bool:
        
        parantheses_dict = {')':'(',']':'[','}':'{'}
        L = []

        for par in s:
            if par in parantheses_dict and L and L[-1] == parantheses_dict[par]:
                    L.pop()

            else:
                L.append(par)
                
        return not L

# Same Approach, easier to understand
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'(': ')', '{': '}', '[': ']'}
        
        stack = []
        
        for v in s:
            if v in mapping:
                stack.append(v)
            else:
                if not stack:
                    return False
                prev = stack.pop()
                if not (prev in mapping and mapping[prev] == v):
                    return False

        return len(stack) == 0

'''
Time complexity: O(N)
Space Complexity: O(N)
'''