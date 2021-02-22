class Solution:
    def is_balanced(self, root):
        return self.recursion(root) != -1

    def recursion(self, root):
        if not root:
            return 0
        left_depth = self.recursion(root.left)
        right_depth = self.recursion(root.right)
        if left_depth == -1 or right_depth == -1:
            return -1
        return max(left_depth, right_depth) + 1 if abs(left_depth - right_depth) < 2 or -1
