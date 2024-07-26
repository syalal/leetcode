class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        if target > matrix[-1][-1]:
            return False

        up, down = 0, rows-1

        while up <= down:
            mid = up + ((down-up)//2)
            if target > matrix[mid][-1]:
                up = mid + 1
            elif target < matrix[mid][0]:
                down = mid - 1
            else:
                break

        if not up <= down:
            return False

        final_row = mid

        l, r = 0, cols-1

        while l <= r:
            mid = l + ((r-l)//2)
            if target > matrix[final_row][mid]:
                l = mid + 1
            elif target < matrix[final_row][mid]:
                r = mid -1
            else:
                break

        if not l <= r:
            return False

        final_col = mid

        return True

        