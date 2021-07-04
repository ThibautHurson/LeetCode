# Solution based on binary seach
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        left = 0
        right = len(nums1)
        half_len = (len(nums1) + len(nums2) + 1) / 2 # the +1 here enable us the code to work with both odd and even scenarios

        while left <= right:
            partition1 = int((right + left) / 2)
            partition2 = int(half_len - partition1)

            # if partition1 is 0 it means nothing is there on left side. Use -inf for maxLeft1
            # if partition1 is length of input then there is nothing on right side. Use +inf for minRight1
            maxLeft1 = nums1[partition1-1] if partition1 != 0 else -float('inf')
            minRight1 = nums1[partition1] if partition1 != len(nums1) else float('inf')
                
            maxLeft2 = nums2[partition2-1] if partition2 != 0 else -float('inf')
            minRight2 = nums2[partition2] if partition2 != len(nums2) else float('inf')

            # If we partitionned at the right place we can return the median
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # If the total length is even
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                else: # the total length is odd so we return the max of the left side as we have one extra element on the left side
                    return max(maxLeft1, maxLeft2)

            elif maxLeft1 > minRight2: # We are too fare on the right side for partition1. Go to the left
                right = partition1 - 1
            else: # We are too far on left side for partitionX. Go to the right.
                left = partition1 + 1

'''
Time: O(log(min(x,y))
Space: O(1)

Explanations:
https://www.youtube.com/watch?v=LPFhl65R7ww&ab_channel=TusharRoy-CodingMadeSimple
'''

nums1 = [1,2]
nums2 = [3,4]

sol = Solution()
print(sol.findMedianSortedArrays(nums1, nums2))



# To recall
def binary_search(target, nums):
    left = 0
    right = len(nums)

    while left != right:
        m = ceil((right + left)/2)
        if nums[m] > target:
            right = m - 1
        else:
            left = m
    if nums[left] == target:
        return left
    return 'Unsuccessful'


    
         