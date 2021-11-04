# Approach 1: bit shifts
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for k in range(32):
            bit = n & 1
            n >>= 1

            res <<= 1
            res += bit
        return res

'''
Time complexity : O(32)
Space complexity : O(1).
'''

n = 4294967293
sol = Solution()
print(sol.reverseBits(n))

