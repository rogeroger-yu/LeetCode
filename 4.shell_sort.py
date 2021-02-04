class Solution:
    def shell_sort(self, nums):
        if not nums:
            return
        size = len(nums)
        gap = size // 2
        while gap >= 1:
            for j in range(gap, size):
                i = j
                while i - gap > 0:
                    if nums[i] < nums[i-gap]:
                        nums[i], nums[i-gap] = nums[i-gap], nums[i]
                        i -= gap
                    else:
                        break
            gap //= 2
        return nums
