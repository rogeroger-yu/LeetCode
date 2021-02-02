class Solution:
    def bubble_sort(self, nums):
        if not nums:
            return
        size = len(nums)
        for i in range(size):
            for j in range(i):
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums
