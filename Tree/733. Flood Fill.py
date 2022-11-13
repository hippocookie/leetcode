from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image or not image[0]:
            return image
        n = len(image)
        m = len(image[0])

        if not 0 <= sr < n or not 0 <= sc < m:
            return image

        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]

        visited = [[False for i in range(m)] for i in range(n)]
        origin_color = image[sr][sc]
        queue: List[List[int]] = [[sr, sc]]
        while queue:
            node: List[int] = queue.pop(0)
            if visited[node[0]][node[1]] or image[node[0]][node[1]] != origin_color:
                continue
            image[node[0]][node[1]] = color
            visited[node[0]][node[1]] = True
            for i in range(4):
                x = node[1] + dx[i]
                y = node[0] + dy[i]
                if 0 <= x < m and 0 <= y < n:
                    queue.append([y, x])
        return image

if __name__ == '__main__':
    # print(Solution().floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))

    print(Solution().floodFill([[0,0,0], [0, 0, 0]], 0, 0, 0))
