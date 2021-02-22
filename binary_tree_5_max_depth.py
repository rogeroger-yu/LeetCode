class Solution:
    def max_depth_BFS(self, root):
        if not root:
            return 0
        tmp, ret = [root], 0
        while tmp:
            ret += 1
            _tmp = []
            for node in tmp:
                if node.left:
                    _tmp.append(node.left)
                if node.right:
                    _tmp.append(node.right)
            tmp = _tmp
        return ret

    def max_depth_DFS(self, root):
        if not root:
            return 0
        else:
            return max(self.max_depth_DFS(root.left), self.max_depth_DFS(root.right)) + 1
