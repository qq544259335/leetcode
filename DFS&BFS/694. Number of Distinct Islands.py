class Solution:
    # same dfs sequence means same island
    def numDistinctIslands(self, grid: [[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        island_set = set()

        def dfs(i, j):
            for k in range(4):
                x, y = directions[k]
                new_i = i + x
                new_j = j + y
                if 0 <= new_i < n and 0 <= new_j < m and grid[new_i][new_j] == 1:
                    grid[new_i][new_j] = 0
                    track.append(str(k))
                    dfs(new_i, new_j)
            return

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    track = []
                    dfs(i, j)
                    serial = "".join(track)
                    if serial not in island_set:
                        res += 1
                        island_set.add(serial)
        return res
