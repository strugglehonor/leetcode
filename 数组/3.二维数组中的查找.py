class Solution:
    def findNumberIn2DArray(self, matrix, target):
        if not matrix:
            return False
        col = len(matrix[0])-1
        row = 0
        while col>=0 and row<len(matrix):  # 这里的边界条件需要特别注意
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False