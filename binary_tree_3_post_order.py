class Solution:
    def post_order_traversal_recursion(self, root):
        res = []
        def recursion(node):
            if not node:
                return
            recursion(node.left)
            recursion(node.right)
            res.append(node.val)
        recursion(root)
        return res

    def post_order_traversal_iteration(self, root):
        res = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.right
            cur = stack.pop()
            cur = cur.left
            return res[::-1]
