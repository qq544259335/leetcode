class Solution:
    def numEnclavesDFS(self, grid: [[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        n = len(grid)
        m = len(grid[0])

        def dfs(i, j, depth):
            if grid[i][j] == 0:
                return
            grid[i][j] = 0
            for x, y in directions:
                new_i = i + x
                new_j = j + y
                if 0 <= new_i < n and 0 <= new_j < m and grid[new_i][new_j] == 1:
                    depth = dfs(new_i, new_j, depth + 1)
            return depth

        for i in range(n):
            if grid[i][0] == 1:
                dfs(i, 0, 0)
            if grid[i][m - 1] == 1:
                dfs(i, m - 1, 0)

        for j in range(m):
            if grid[0][j] == 1:
                dfs(0, j, 0)
            if grid[n - 1][j] == 1:
                dfs(n - 1, j, 0)

        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    res += dfs(i, j, 1)

        return res

    def numEnclavesBFS(self, grid: [[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        n = len(grid)
        m = len(grid[0])
        queue = []

        def bfs(i, j):
            queue.append((i, j))
            grid[i][j] = 0
            breadth = 1
            while queue:
                length = len(queue)
                for _ in range(length):
                    x, y = queue.pop(0)
                    for xx, yy in directions:
                        new_i, new_j = x + xx, y + yy
                        if 0 <= new_i < n and 0 <= new_j < m and grid[new_i][new_j] == 1:
                            grid[new_i][new_j] = 0
                            queue.append((new_i, new_j))
                            breadth += 1
            return breadth

        for i in range(n):
            if grid[i][0] == 1:
                bfs(i, 0)
            if grid[i][m - 1] == 1:
                bfs(i, m - 1)

        for j in range(m):
            if grid[0][j] == 1:
                bfs(0, j)
            if grid[n - 1][j] == 1:
                bfs(n - 1, j)

        res = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    res += bfs(i, j)
        return res
