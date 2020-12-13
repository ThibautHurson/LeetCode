class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return None
        res= []
        queue = collections.deque([(root,0)])
        
        while queue:
            head,level = queue.popleft()
            
            if len(res)-1 < level:
                res.append([head.val])
            else:
                res[level].append(head.val)
        
            if head.left:
                queue.append((head.left,level+1))
            if head.right:
                queue.append((head.right,level+1))
        
        return res
'''
Je pense :
Time: O(n)
Space: O(n) in the case of skewed binary tree.
'''