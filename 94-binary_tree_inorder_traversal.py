class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        head = root
        while stack or head:
            while head:
                stack.append(head)
                head = head.left
                       
            head = stack.pop()
            res.append(head.val)
            
            head = head.right

        return res
'''
Rq: On aurait aussi pu le faire de manière récursive avec les mêmes complexités
Time: O(n)
Space: O(n)
'''