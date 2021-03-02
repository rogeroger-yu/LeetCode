class Solution:
    # DFS
    def dfs(self, root, sum):
        if not root:
            return False
        if not root.right and not root.left:
            return sum == root.val
        return self.dfs(root.right, sum-root.val) or self.dfs(root.left, sum-root.val)

    # BFS 队列
    def bfs(self, root, sum):
        if not root:
            return False
        stack = []
        stack.append((root, root.val))
        while stack:
            node, path_sum = stack.pop(0)
            if not node.left and not node.right and path_sum == sum:
                return True
            if node.left:
                stack.append((node.left, path_sum+node.left.val))
            if node.right:
                stack.append((node.right, path_sum+node.right.val))
        return False

    # 栈
    def bfs(self, root, sum):
        if not root:
            return False
        stack = []
        stack.append((root, root.val))
        while stack:
            # 和上面的算法仅这行不同，但是结果是一致的，前者为先序遍历，后者为中->右->左
            node, path_sum = stack.pop()
            if not node.left and not node.right and path_sum == sum:
                return True
            if node.left:
                stack.append((node.left, node.left.val))
            if node.right:
                stack.append((node.right, node.right.val))
        return False
