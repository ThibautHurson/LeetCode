import collections

# Approach: BFS
class Solution:
	def isValidBST(self, root):
		queue = collections.deque()
		queue.append((-float('inf'), root, float('inf')))

		while queue:
			valmin, curr, valmax = queue.popleft()
			if valmin >= curr.val or curr.val >= valmax:
				return False

			if curr.left:
				queue.append((valmin, curr.left, curr.val))

			if curr.right:
				queue.append((curr.val, curr.right, valmax))

		return True

'''
Time complexity: O(N) where N is the given number of nodes in BST
Space complexity: O(N)

Note: A lot of developers used DFS
'''