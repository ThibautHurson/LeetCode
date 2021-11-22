# DFS
class Solution:
	def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
		self.ans = 0

		def dfs(head):
			if not head:
				return 0

			left, right = dfs(head.left), dfs(head.right)  
			self.ans = max(left + right, self.ans)
			return max(left, right) + 1

		dfs(root)
		return self.ans

'''
Time complexity : O(N), where N is a number of nodes in the tree, since one visits each node exactly once.
Space complexity : O(log(N)) in the best case of completely balanced tree and O(N) in the worst case of completely unbalanced tree, to keep a recursion stack.
'''