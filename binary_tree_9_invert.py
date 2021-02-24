class Solution:
    def invert_recursion(self, root):
        def recursion(node):
            if not node:
                return
            node.left, node.right = node.right, node.left
            recursion(node.left)
            recursion(node.right)
            return node
        return recursion(root)

    def invert_iteration(self, root):
        if not root:
            return
        if not root.left and not root.right:
            return root
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop(0)
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root
