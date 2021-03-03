class Solution:
    def spiralOrder_myself(self, matrix):
        high = len(matrix)
        wide = len(matrix[0])
        length = high * wide
        res = []
        i, j = 0, 0 
        direction = 0
        left_border = 0
        right_border = wide - 1
        top_border = 1
        botton_border = high - 1
        for _ in range(length):
            #import pdb;pdb.set_trace()
            res.append(matrix[i][j])
            if direction == 0 and j < right_border:
                j += 1
            elif direction == 0 and j == right_border:
                direction += 1
                right_border -= 1
                i += 1
                continue

            if direction == 1 and i < botton_border:
                i += 1
            elif direction == 1 and i == botton_border:
                direction += 1
                botton_border -= 1
                j -= 1
                continue

            if direction == 2 and j > left_border:
                j -= 1
            elif direction == 2 and j == left_border:
                direction += 1
                left_border += 1
                i -= 1
                continue

            if direction == 3 and i > top_border:
                i -= 1
            elif direction == 3 and i == top_border:
                direction = 0
                top_border += 1
                j += 1
                continue
        return res

    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        rows, columns = len(matrix), len(matrix[0])
        order = []
        left, right, top, botton = 0, columns - 1, 0, rows - 1
        while left <= right and top <= botton:
            for column in range(left, right + 1):
                order.append(matrix[top][column])
            for row in range(top + 1, botton + 1):
                order.append(matrix[row][right])
            if left < right and top < botton:
                for column in range(right - 1, left, -1):
                    order.append(matrix[botton][column])
                for row in range(botton, top, -1):
                    order.append(matrix[row][left])
            left, right, top, botton = left + 1, right - 1, top + 1, botton - 1
        return order
