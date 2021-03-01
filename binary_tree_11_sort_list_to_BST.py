class Solution:
    def sort_list_to_BST(self, head):
        if not head:
            return
        pre, slow, fast = None, head, head
        while fast and fast.next:
            fast = fast.next.next
            pre = slow
            slow = slow.next
        if pre:
            pre.next = None
        node = TreeNode(slow.val)
        if slow == fast:
            return node
        node.left = self.sort_list_to_BST(head)
        node.right = self.sort_list_to_BST(slow.next)
        return node
