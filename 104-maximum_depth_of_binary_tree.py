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