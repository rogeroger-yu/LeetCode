class Solution:
    def level_order_BFS(self, root):
        queue = []
        res = []
        queue.append(root)
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                node = queue.pop(0)
                if not node:
                    continue
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            if level:
                res.append(level)
        return res

    def level_order_DFS(self, root):
        res = []
        self.level(root, 0, res)
        return res

    def level(self, root, level, res):
        if not root:
            return
        if len(res) == level:
            res.append([])
        res[level].append(root.val)
        if root.left:
            self.level(root.left, level + 1, res)
        if root.right:
            self.level(root.right, level + 1, res)
