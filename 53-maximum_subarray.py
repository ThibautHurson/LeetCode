#Dynamic program. See  https://www.youtube.com/watch?v=2MmGzdiKR9Y 
#Also https://en.wikipedia.org/wiki/Maximum_subarray_problem
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:     
        current_sum = best_sum = nums[0]
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            best_sum = max(best_sum, current_sum)
        return best_sum

'''
Time complexity: O(N)
Space complexity: O(1)
'''

# Same Idea, a bit different
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:     
        res = nums[0]
        for i in range(1,len(nums)):
            nums[i] = max(nums[i], nums[i]+nums[i-1])
        return max(nums)


#Divide and Conquer
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def dnc(nums, l, r):
            if not nums or r < l:
                return 0, 0, 0, 0
            if l == r:
                return nums[l], nums[l], nums[l], nums[l]
            m = (l + r) // 2
            ll, lr, lm, ls = dnc(nums, l, m)  # left max, right max, mid max, sum of left
            rl, rr, rm, rs = dnc(nums, m+1, r)  # left max, right max, mid max, sum of right
            ml = max(ll, ls + rl)
            mr = max(rr, rs + lr)
            mm = max(lm, rm, lr + rl)
            ms = ls + rs
            return ml, mr, mm, ms  # left max, right max, mid max, sum of merge
        
        return dnc(nums, 0, len(nums)-1)[2]