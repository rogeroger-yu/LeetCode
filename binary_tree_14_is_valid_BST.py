class Solution:
    def is_valid_BST(self, root):
        def _recur(node, min_val, max_val):
            if not node:
                return True
            if not min_val < node.val < max_val:
                return False
            return _recur(node.left, min_val, node.val) and _recur(node.right, node.val, max_val)
        return _recur(root, float('-inf'), float('inf'))
