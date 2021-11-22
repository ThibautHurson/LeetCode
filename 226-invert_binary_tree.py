# Breath-First Search (BFS)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        queue = collections.deque([root])

        while queue:
            head = queue.popleft()
            head.left, head.right = head.right, head.left
            
            if head.left:
                queue.append(head.left)
                
            if head.right:
                queue.append(head.right)
                
        return root

'''
Time complexity : O(N) since each node is visited exactly once.
Space complexity : O(log(N)) in the best case of completely balanced tree and O(N) in the worst case of completely unbalanced tree, to keep a deque.
'''

# Depth First Search
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        def reorder(head):
            head.left, head.right = head.right, head.left

            if head.left:
                reorder(head.left)
            if head.right:
                reorder(head.right)

        reorder(root)
        return root

'''
Time complexity : O(N), where N is a number of nodes in the tree, since one visits each node exactly once.
Space complexity : O(log(N)) in the best case of completely balanced tree and O(N) in the worst case of completely unbalanced tree, to keep a recursion stack.
'''