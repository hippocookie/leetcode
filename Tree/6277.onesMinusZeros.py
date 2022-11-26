from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        one_row = [0 for i in range(m)]
        one_col = [0 for i in range(n)]
        result = [[0 for i in range(n)] for j in range(m)]
        for i in range(0, m):
            one_count = 0
            for j in range(0, n):
                if grid[i][j] == 1:
                    one_count += 1
            one_row[i] = one_count

        for i in range(0, n):
            one_count = 0
            for j in range(0, m):
                if grid[j][i] == 1:
                    one_count += 1
            one_col[i] = one_count

        for i in range(0, m):
            for j in range(0, n):
                result[i][j] = one_row[i] + one_col[j] - (m - one_row[i]) - (n - one_col[j])
        return result



if __name__ == '__main__':
    print(Solution().onesMinusZeros([[0,1,1],[1,0,1],[0,0,1]]))