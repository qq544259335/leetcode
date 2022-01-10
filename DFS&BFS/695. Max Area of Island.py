class Solution:
    def maxAreaOfIsland(self, grid: [[int]]) -> int:
        queue = []
        n = len(grid)
        m = len(grid[0])
        res = 0
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    grid[i][j] = 0
                    breadth = 1
                    while queue:
                        length = len(queue)
                        for _ in range(length):
                            cur_i, cur_j = queue.pop(0)
                            for x, y in directions:
                                new_i = cur_i + x
                                new_j = cur_j + y
                                if 0 <= new_i < n and 0 <= new_j < m and grid[new_i][new_j] == 1:
                                    grid[new_i][new_j] = 0
                                    queue.append((new_i, new_j))
                                    breadth += 1
                    res = max(res, breadth)
        return res
