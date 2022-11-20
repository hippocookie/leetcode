from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if not matrix or not matrix[0]:
            return result
        row = len(matrix)
        col = len(matrix[0])
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        visited = -1000
        x = 0
        y = 0
        direct_index = 0
        for i in range(row * col):
            result.append(matrix[y][x])
            matrix[y][x] = visited
            tx = x + dx[direct_index]
            ty = y + dy[direct_index]
            if tx < 0 or ty < 0 or tx > col - 1 or ty > row - 1 or matrix[ty][tx] == visited:
                direct_index = (direct_index + 1) % 4
            x = x + dx[direct_index]
            y = y + dy[direct_index]
        return result


if __name__ == '__main__':
    # print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

    print(Solution().spiralOrder([[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16]]))
