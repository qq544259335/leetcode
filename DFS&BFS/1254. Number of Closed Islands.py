class Solution:
    # based on 200, the only difference is that first find the island on the borders and don't count them
    def closedIsland(self, grid: [[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(i, j):
            if grid[i][j] == 1:
                return
            grid[i][j] = 1
            for x, y in directions:
                new_i = i + x
                new_j = j + y
                if 0 <= new_i < n and 0 <= new_j < m and grid[new_i][new_j] == 0:
                    dfs(new_i, new_j)
            return

        for i in range(n):
            if grid[i][0] == 0:
                dfs(i, 0)
            if grid[i][m - 1] == 0:
                dfs(i, m - 1)

        for j in range(m):
            if grid[0][j] == 0:
                dfs(0, j)
            if grid[n - 1][j] == 0:
                dfs(n - 1, j)
        print(grid, res)
        for i in range(1, n):
            for j in range(1, m):
                if grid[i][j] == 0:
                    dfs(i, j)
                    res += 1
        return res


solve = Solution()
print(solve.closedIsland(
    [[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1],
     [1, 1, 1, 1, 1, 1, 1, 0]]))
