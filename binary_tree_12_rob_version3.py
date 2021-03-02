class Solution:
    def rob3(self, root):
        def _rob(node):
            if not node:
                return 0, 0
            left = _rob(node.left)
            right = _rob(node.right)
            v1 = node.val + left[1] + right[1]
            v2 = max(left) + max(right)
            return v1, v2
        return max(_rob(root))
