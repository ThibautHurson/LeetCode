# Binary Search of left index. Then right index goes incrementally to right.
#Note: Approch 2 is best before in the worst case in which the list only contains target --> time complexity O(N)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if (not nums) or (nums[-1] < target) or (nums[0] > target):
            return [-1,-1]
        

        
        def get_left(nums, target, left, right, fin_left):

            while left < right:
                mid = (left + right)//2

                if nums[mid] > target or (fin_left and nums[mid] == target):
                    right = mid 
                if nums[mid] < target or (not fin_left and nums[mid] == target):
                    left = mid + 1
            return left
        
       
        left = get_left(nums, target, 0, len(nums)-1, True)
        if nums[left] != target:
            return [-1,-1]
        
        right = get_left(nums, target, left, len(nums)-1, True)
        while right <= len(nums)-1 and nums[right] == target:
            right += 1
            
        return [left,right-1]

#Two binary search
class Solution:
    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
    def searchRange(self, nums, target):
        def search(n):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] >= n:
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        lo = search(target)
        return [lo, search(target+1)-1] if target in nums[lo:lo+1] else [-1, -1]

'''
Time complexity : O(logN)

Space complexity : O(1)

All work is done in place, so the overall memory usage is constant.
'''