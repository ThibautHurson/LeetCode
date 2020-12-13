class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
        end = False
        n = len(strs)
        length = len(strs[0])
        for i in range(1,n):
            length = min(length,len(strs[i]))
        if length == 0:
            return ""
        
        i_max = 0
        while True:
            a = strs[0][i_max]
            for k in range(1,n):
                if strs[k][i_max] != a:
                    end = True
                    break
            if end: break
            i_max += 1
            if i_max == length:break
            
        return strs[0][:i_max]