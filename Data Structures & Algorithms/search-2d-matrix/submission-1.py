class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        left, right = 0, m-1
        while left <= right:
            row_mid = (left + right) // 2
            if matrix[row_mid][0] > target:
                right = row_mid - 1
            elif matrix[row_mid][-1] < target:
                left = row_mid + 1
            else:
                break
        
        row = (left + right) // 2
        left, right = 0, n-1 
        while left <= right:
            col_mid = (left + right) // 2
            if matrix[row][col_mid] < target:
                left = col_mid + 1
            elif matrix[row][col_mid] > target:
                right = col_mid - 1
            else:
                return True
        return False