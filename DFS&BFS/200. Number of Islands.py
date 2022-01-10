class Solution:
    # because 0 and visited both mean don't visit, so merge them in one
    def numIslandsDFS(self, grid: [[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(i, j):
            for x, y in directions:
                new_i = i + x
                new_j = j + y
                if 0 <= new_i < n and 0 <= new_j < m and grid[new_i][new_j] == "1":
                    grid[new_i][new_j] = "0"
                    dfs(new_i, new_j)
            return

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
        return res

    def numIslandsBFS(self, grid: [[str]]) -> int:
        queue = []
        n = len(grid)
        m = len(grid[0])
        res = 0
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    queue.append((i, j))
                    while queue:
                        length = len(queue)
                        for _ in range(length):
                            cur_i, cur_j = queue.pop(0)
                            for x, y in directions:
                                new_i = cur_i + x
                                new_j = cur_j + y
                                if 0 <= new_i < n and 0 <= new_j < m and grid[new_i][new_j] == "1":
                                    grid[new_i][new_j] = "0"
                                    queue.append((new_i, new_j))
                    res += 1
        return res


solve = Solution()
print(solve.numIslandsBFS(
    [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
