from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        n = len(grid)
        m = len(grid[0])
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]
        counter = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "Y":
                    continue
                if grid[i][j] == "1":
                    counter += 1
                    queue = [[i, j]]
                    while queue:
                        node = queue.pop(0)
                        for k in range(4):
                            x = node[1] + dx[k]
                            y = node[0] + dy[k]
                            if 0 <= x < m and 0 <= y < n and grid[y][x] == "1":
                                grid[y][x] = "Y"
                                queue.append([y, x])
        return counter

if __name__ == '__main__':
    print(Solution().numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))
