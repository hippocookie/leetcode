from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        row = len(grid)
        col = len(grid[0])

        def is_blocked(x, y, val):
            if val == 1 and (x == col - 1 or grid[y][x + 1] == -1):
                return True
            elif val == -1 and (x == 0 or grid[y][x - 1] == 1):
                return True
            else:
                return False

        result = list()
        for i in range(col):
            x = i
            y = 0
            while y < row:
                if x < 0 or x >= col or is_blocked(x, y, grid[y][x]):
                    result.append(-1)
                    break
                x = x + grid[y][x]
                y += 1
            if y == row:
                result.append(x)
        return result




if __name__ == '__main__':
    print(Solution().findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]))
    print(Solution().findBall([[-1]]))
