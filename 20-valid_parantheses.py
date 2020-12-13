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
