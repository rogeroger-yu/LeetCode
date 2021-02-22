class Solution:
    def is_symmetric(self, root):
        if not root:
            return True
        pre_order_res = self.pre_order(root)
        post_order_res = self.post_order(root)
        if pre_order_res == post_order_res[::-1]:
            return True
        else:
            return False

    def pre_order(self, root):
        res = []
        def recursion(node):
            if not node:
                res.append(None)
                return
            res.append(node.val)
            recursion(node.left)
            recursion(node.right)
        recursion(root)
        return res

    def post_order(self, root):
        res = []
        def recusrion(node):
            if not node:
                res.append(None)
                return
            recursion(node.left)
            recursion(node.right)
            res.append(node.val)
        recursion(root)
        return res
