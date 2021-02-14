class Solution:
    def inorderTraversial_recursion(self, root):
        res = []
        def recursion(node):
            if not node:
                return
            recursion(node.right)
            res.append(node.val)
            recursion(node.left)
        recursion(root)
        return res

    def inorderTraversial_iteration(self, root):
        res = []
        stack = [root]
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur.left)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res
