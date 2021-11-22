# DFS / Recursion: By creating a new tree
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(head, head1, head2):
            head.val = (head1!=None and head1.val) + (head2!=None and head2.val)

            if (head1 and head1.left) or (head2 and head2.left):
                head.left = TreeNode()
                dfs(head.left, (head1 and head1.left), (head2 and head2.left))
            if (head1 and head1.right) or (head2 and head2.right):
                head.right = TreeNode()
                dfs(head.right, (head1 and head1.right), (head2 and head2.right))

        if not root1 and not root2:
            return None

        root = TreeNode()
        dfs(root, root1, root2)

        return root

# Recursion:  Inplace in one of the trees
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:        
        if not root1:
            return root2
        if not root2:
            return root1

        root1.val += root2.val

        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1


'''
Time complexity : O(m). A total of m nodes need to be traversed. Here, m represents the 
minimum number of nodes from the two given trees.

Space complexity : O(m). The depth of the recursion tree can go upto m in the case of a 
skewed tree. In average case, depth will be O(log(m)).
'''
