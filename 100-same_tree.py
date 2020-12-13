#Approch 1: DFS
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        return self.search(p,q)
            
        
    def search(self,p,q):
        if not p and not q:
            return True
        
        if (not p or not q) or (p.val != q.val):
            return False
   
        return self.search(p.left,q.left) and self.search(p.right,q.right)

'''
Time complexity : \mathcal{O}(N)O(N), where N is a number of nodes in the tree, since one visits each node exactly once.
Space complexity : \mathcal{O}(\log(N))O(log(N)) in the best case of completely balanced tree and \mathcal{O}(N)O(N) in the worst case of completely unbalanced tree, to keep a recursion stack.
'''
#Approch 2: Iterative
from collections import deque
class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """    
        def check(p, q):
            # if both are None
            if not p and not q:
                return True
            # one of p and q is None
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            return True
        
        deq = deque([(p, q),])
        while deq:
            p, q = deq.popleft()
'''
Time complexity : \mathcal{O}(N)O(N) since each node is visited exactly once.
Space complexity : \mathcal{O}(\log(N))O(log(N)) in the best case of completely balanced tree and \mathcal{O}(N)O(N) in the worst case of completely unbalanced tree, to keep a deque.
'''