class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        if not nums:
            return None
        
        idx_mid = len(nums)//2
              
        root = TreeNode(nums[idx_mid])

        root.left = self.sortedArrayToBST(nums[:idx_mid])
        root.right = self.sortedArrayToBST(nums[idx_mid+1:])
        
        return root
'''
comme c'est couteux de slicer un array, il vaut mieux passer en arg left et right
it takes O(n) to slice, making the entire algorithm O(n logn)'''

class Solution(object):
    def sortedArrayToBST(self, nums):
        def convert(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = convert(left, mid - 1)
            node.right = convert(mid + 1, right)
            return node
        return convert(0, len(nums) - 1)
'''
Time: O(n)
Space: O(n) in the case of skewed binary tree.
'''