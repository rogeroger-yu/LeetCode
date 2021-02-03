class Solution:
    def selection_sort(self, nums):
        if not nums:
            return
        size = len(nums)
        for i in range(size):
            min_index = i
            for j in range(i+1, size):
                if nums[min_index] > nums[j]:
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]
        return nums
