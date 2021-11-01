# DFS
class Solution:
    def maxPathSum(self, root):
        self.max_path = float('-inf')

        def get_max_gain(node):
            if not node:
                return 0

            gain_l = max(get_max_gain(node.left), 0)
            gain_r = max(get_max_gain(node.right), 0)

            curr_max_path = node.val + gain_l + gain_r
            self.max_path = max(self.max_path, curr_max_path)

            return node.val + max(gain_l, gain_r)

        get_max_gain(root)
        return self.max_path

