# Approach 1: Dynamic Programming
class Solution:
    def generate(self, numRows):
        if not numRows:
            return []
        elif numRows == 1:
            return [[1]]

        n = 1
        res = [[1]]
        while n < numRows:
            cur = [1]
            for i in range(1, len(res[-1])):
                cur.append(res[-1][i-1] + res[-1][i])
            cur.append(1)
            res.append(cur)
            n += 1
        return res

sol = Solution()
print(sol.generate(5))
