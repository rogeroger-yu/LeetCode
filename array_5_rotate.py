class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        new_nums = [0]*length
        for i in range(length):
            new_nums[(i+k)%length] = nums[i]
        nums = new_nums
        print(new_nums)

    def rotate2(self, nums, k):
        length = len(nums)
        k = k % length
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        reverse(0, k)
        reverse(k+1, length-1)
        reverse(0, length-1)
        print(nums)

    def rotate3(self, nums, k):
        length = len(nums)
        k = k % length
        cnt = 0
        start = 0
        while cnt < length:
            current = start
            pre = nums[current]
            while True:
                nxt = (current + k) % length
                nums[nxt], pre = pre, nums[nxt]
                current = nxt
                cnt += 1
                if current == start:
                    break
            start += 1
        print(nums)

a=Solution()
a.rotate3([1,2,3,4,5,6,7], 3)
