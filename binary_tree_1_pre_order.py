class Solution:
    def pre_order_traversal_recursion(self, root):
        res = []
        def recursion(node):
            if not node:
                return
            res.append(node.value)
            recursion(node.left)
            recursion(node.right)
        recursion(root)
        return res

    def pre_order_traversal_iteration(self, root):
        res = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.value)
            cur = cur.right
        return res
