# Approach: Backtracking
class Solution:
    def combinationSum(self, candidates, target):
        self.combination = []
        self.candidates = candidates
        candidates.sort()

        def backtrack(start, curr, target):
            if target == 0:
                self.combination.append(curr)
                return

            for k in range(start, len(self.candidates)):
                val = self.candidates[k]
                if target - val < 0:
                    return
                curr.append(val)
                backtrack(k, curr.copy(), target - val)
                curr.pop()

        backtrack(0, [], target)

        return self.combination

candidates = [2,3,6,7]
target = 7
sol = Solution()
print(sol.combinationSum(candidates, target))