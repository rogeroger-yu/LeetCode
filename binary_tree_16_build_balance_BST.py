class Solution:
    def balance_BST(self, root):
        return self.build_tree(self.inOrder(root))

    def inOrder(self, node):
        if not node:
            return []
        return self.inOrder(node.left) + [node.val] + self.inOrder(node.right)

    def build_tree(self, node_list):
        length = len(node_list)
        if length == 0:
            return None
        if length == 1:
            return TreeNode(node_list.pop())
        mid = length // 2
        node = TreeNode(node_list[mid])
        node.left = self.build_tree([:mid])
        node.right = self.build_tree([mid+1:])
        return node
