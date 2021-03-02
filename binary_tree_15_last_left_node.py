class Solution:
    # 层序遍历
    def last_left_node(self, root):
        if not root:
            return None
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop(0)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return node.val

    # 深度优先算法
    def last_left_node(self, root):
        def _recur(node, depth):
            if not node:
                return None
            if self.max_depth < depth:
                self.max_depth = depth
                self.res = node.val
            _recur(node.left, depth+1)
            _recur(node.right, depth+1)
        self.max_depth, self.res = -1, 0
        _recur(root, 0)
        return self.res
        
