from collections import deque


class Solution:
    def numIslands1(self, grid: [[str]]) -> int:
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
                                for nx, ny in [[x + 1, y], [x, y + 1], [x - 1, y], [x, y - 1]]:
                                    if 0 <= nx <= len(grid) - 1 and 0 <= ny <= len(grid[0]) - 1 and (
                                            nx, ny) not in visited:
                                        if grid[nx][ny] == "1":
                                            queue.append((nx, ny))
                                        elif grid[nx][ny] == "0":
                                            visited.add((nx, ny))
                            visited.add(cur)
                        res += 1
        return res

    def numIslands(self, grid: [[str]]) -> int:
        count = 0
        height = len(grid)
        length = len(grid[0])
        for i in range(height):
            for j in range(length):
                if grid[i][j] == '1':
                    cur_islands = [(i, j)]
                    grid[i][j] = True
                    while cur_islands:
                        cur = cur_islands.pop(0)
                        x, y = cur
                        for (new_x, new_y) in [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]:
                            if 0 <= new_x < height and 0 <= new_y < length and grid[new_x][new_y] == '1':
                                grid[new_x][new_y] = True
                                cur_islands.append((new_x, new_y))
                    count += 1
        return count


solve = Solution()
print(solve.numIslands(
    [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
