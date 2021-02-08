from collections import deque

class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        visited = set()
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited:
                    if grid[i][j] == "0":
                        visited.add((i, j))
                    else:
                        queue = deque()
                        queue.append((i, j))
                        while queue:
                            cur = queue.popleft()
                            if cur not in visited:
                                x, y = cur[0], cur[1]
                                for nx, ny in [[x + 1, y],[x, y + 1],[x - 1, y], [x, y - 1]]:
                                    if 0 <= nx <= len(grid) - 1 and 0 <= ny <= len(grid[0]) - 1 and (nx, ny) not in visited:
                                        if grid[nx][ny] == "1":
                                            queue.append((nx, ny))
                                        elif grid[nx][ny] == "0":
                                            visited.add((nx, ny))
                            visited.add(cur)
                        res += 1
        return res

solve = Solution()
print(solve.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
