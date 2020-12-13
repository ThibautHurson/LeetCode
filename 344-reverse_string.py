class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        med = n//2
        
        for k in range (med):
            s[k],s[n-k-1] = s[n-k-1],s[k]

'''
Time complexity : O(N) to swap N/2 element.

Space complexity : O(1), it's a constant space solution.
'''