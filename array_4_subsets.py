class Solution:
    # 迭代
    def subsets(self, nums):
        res = [[]]
        for i in nums:
            res = res + [[i] + n for n in res]
        return res

    # 递归
    def subsets(self, nums):
        length = len(nums)
        res = []
        def helper(index, tmp):
            res.append(tmp)
            for new_index in range(index, length):
                helper(new_index + 1, tmp + [nums[new_index]])
        helper(0, [])
        return res
