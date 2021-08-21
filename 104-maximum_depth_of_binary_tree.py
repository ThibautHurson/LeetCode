# DFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.max_length = 0
        self.search(root,0)
        return self.max_length
        
    def search(self,root,length):
        if not root:
            self.max_length = max(self.max_length, length)
            return 
        
        length += 1
        
        self.search(root.left,length)
        self.search(root.right,length)

#BFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = collections.deque()
        queue.append((1, root))
        
        while queue:
            depth, head = queue.popleft()
            if head.left:
                queue.append((depth+1, head.left))        
            if head.right:
                queue.append((depth+1, head.right))
        return depth
'''
Time complexity: O(N) we go through all nodes
Space complexity: O(N) worst case. When you have one root and all other nodes are this 
        root children, then the queue will append every children 
'''

class Solution:
    def maxDepth(self, root):
        self.maxdepth = 0
        if not root:
            return 0

        if root.left:
            search(0, root.left)
        if root.right:
            search(0, root.right)

        def search(depth, head):
            if not head:




