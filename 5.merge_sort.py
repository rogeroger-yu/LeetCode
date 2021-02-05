class Solution:
    def merge_recursion_sort(self, nums):
        if nums <= 1:
            return nums
        mid = len(nums) // 2
        left = merge_sort(nums[:mid])
        right = merge_sort(nums[mid:])

        result = []
        while left and right:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result.extend(left if left else right)
        return result

    def merge_iteration_sort(self, nums):
        if nums <= 1:
            return nums
        length = len(nums)
        gap = 1
        while gap < length:
            left = 0
            while left < length:
                mid = low + gap
                right = min(left + 2 * gap, length)
                if mid < right:
                    merge(nums, left, mid, right)
                left += 2 * gap
            gap *= 2
        return nums

    def merge(self, nums, left, mid, right):
        left_nums = nums[left:mid]
        right_nums = nums[mid:right]
        k = 0
        j = 0
        result = []
        while k < len(left_nums) and j < len(right_nums):
            if left_nums[k] <= right_nums[j]:
                result.append(left_nums[k])
                k += 1
            else:
                result.append(right_nums[j])
                j += 1
        result += left_nums[k:]
        result += right_nums[j:]
        nums[left:right] = result
