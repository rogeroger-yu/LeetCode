class Solution:
    def set_zero(self, matrix):
        zero_in_first_col = False
        rows = len(matrix)
        columns = len(matrix[0])
        for row in range(rows):
            if matrix[row][0] == 0:
                zero_in_first_col = True
            for column in range(1, columns):
                if matrix[row][column] == 0:
                    matrix[row][0] = 0
                    matrix[0][column] = 0
        for row in range(1, rows):
            for column in range(1, columns):
                if matrix[row][0] == 0 or matrix[0][column] == 0:
                    matrix[row][column] = 0
        if matrix[0][0] == 0:
            for column in range(columns):
                matrix[0][column] = 0
        if zero_in_first_col:
            for row in range(rows):
                matrix[row][0] = 0
