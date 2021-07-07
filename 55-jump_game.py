class Solution:
    def canJump(self, nums):
        last = len(nums) - 1

        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= last:
                last = i
        return last == 0



# DFS but inefficient
class Solution:
    def canJump(self, nums):
        self.visited = set([])
        self.length = len(nums)-1
        self.nums = nums
        self.found = False
        self.search(0)
        return self.found
    def search(self, idx):
        if idx == self.length:
            self.found = True

        self.visited.add(idx)
        for i in range(1,self.nums[idx]+1):
            i_min = min(idx + i, self.length)
            if i_min not in self.visited:
                self.search(i_min)

        
        


nums = [2,3,1,1,4]#[3,2,1,0,4]
sol = Solution()
print(sol.canJump(nums))