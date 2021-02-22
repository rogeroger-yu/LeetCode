class Solution:
    def min_depth_BFS(self, root):
        if not root:
            return 0
        rec = [(root, 1)]
        while rec:
            node, depth = rec.pop(0)
            if not node.left and not node.right:
                return depth
            if node.left:
                rec.append((node.left, depth+1))
            if node.right:
                rec.append((node.right, depth+1))

    def min_depth_DFS(self, root):
        if not root:
            return 0
        res = 0
        if not root.left and not root.right:
            res = 1
        elif root.left and root.right:
            res = min(self.min_depth_DFS(root.left), self.min_depth_DFS(root.right))
        elif root.left:
            res = self.min_depth_DFS(root.left)
        elif root.right:
            res = self.min_depth_DFS(root.right)
        return res
