class Solution:
    def sort_array_to_BST(self, nums):
        if not nums:
            return
        mid = (len(nums) - 1) // 2
        root = TreeNode(nums[mid])
        root.left = self.sort_array_to_BST(nums[:mid])
        root.right = self.sort_array_to_BST(nums[mid+1:])
        return root
