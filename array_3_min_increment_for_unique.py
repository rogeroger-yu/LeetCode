class Solution:
    # 暴力解法，当数组元素都为1，则复杂度将上升到O(n^2)
    def minIncrementForUnique_myself(self, nums):
        unique_list = []
        repeat_list = []
        res = 0
        for i in nums:
            if i not in unique_list:
                unique_list.append(i)
            else:
                repeat_list.append(i)
        for j in repeat_list:
            while j in unique_list:
                j, res = j + 1, res + 1
            unique_list.append(j)
        return res

    def minIncrementForUnique(self, nums):
        count = [0] * 8000
        for i in nums:
            count[i] += 1
        res = taken = 0
        for x in range(8000):
            if count[x] >= 2:
                taken = count[x] - 1
                res -= x * (count[x] - 1)
            elif taken > 0 and count[x] == 0:
                taken -= 1
                res += x
        return res
