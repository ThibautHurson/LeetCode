# Approach 1: collections.Counter
import collections
class Solution:
    def majorityElement(self, nums):
        return collections.Counter(nums).most_common(1)[0][0]

'''
Time complexity : O(n)

We iterate over nums once and make a constant time HashMap insertion on 
each iteration. Therefore, the algorithm runs in O(n)O(n) time.

Space complexity : O(n)
'''
# Approach 2: sort 
class Solution:
    def majorityElement(self, nums):
        nums.sort()  
        return nums[len(nums) // 2]

'''
Time complexity : O(nlog(n))

Space complexity : O(1) or (O(n)O(n))

We sorted nums in place here - if that is not allowed, then we must spend 
linear additional space on a copy of nums and sort the copy instead.
'''