#Approach 1: Recursive
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root,root)
        
    
    def isMirror(self,node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        
        return (node1.val==node2.val) & self.isMirror(node1.left,node2.right) & \
            self.isMirror(node1.right,node2.left)
'''
Time complexity : O(n). Because we traverse the entire input tree once, the total run time is 
O(n), where nn is the total number of nodes in the tree.

Space complexity : The number of recursive calls is bound by the height of the tree. In the worst 
case, the tree is linear and the height is in O(n). Therefore, space complexity due to recursive 
calls on the stack is O(n) in the worst case.
'''
#Approach 2: Iterative
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        queue = collections.deque([root,root])        
        
        while queue:
            node1 = queue.popleft()
            node2 = queue.popleft()
            
            if node1 is None and node2 is None:
                continue
                
            if node1 is None or node2 is None:
                return False
            
            if node1.val != node2.val:
                    return False
                
            queue.append(node1.left)
            queue.append(node2.right)
            queue.append(node1.right)
            queue.append(node2.left)
                
        return True
'''
Time complexity: same
Space complexity : There is additional space required for the search queue. In the worst case, we 
have to insert O(n) nodes in the queue. Therefore, space complexity is O(n).
'''