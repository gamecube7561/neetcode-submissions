class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        matrix_num = -1

        for i, mat in enumerate(matrix):
            if mat[0] <= target and mat[-1] >= target:
                matrix_num = i

        if matrix_num == -1:
            return False

        l = 0
        r = len(matrix[0])

        while l <= r:
            mid = (l + r) // 2

            if matrix[matrix_num][mid] > target:
                r = mid - 1
            elif matrix[matrix_num][mid] < target:
                l = mid + 1

            if matrix[matrix_num][mid] == target:
                return True

        return False
