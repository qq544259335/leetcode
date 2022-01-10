class Solution:
    # an island is sub == all node in grid2 is 1 is also 1 in grid1
    def countSubIslands(self, grid1: [[int]], grid2: [[int]]) -> int:
        queue = []
        n = len(grid1)
        m = len(grid1[0])
        res = 0
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for i in range(n):
            for j in range(m):
                if grid2[i][j] == 1:
                    is_sub = True
                    queue.append((i, j))
                    grid2[i][j] = 0
                    while queue:
                        length = len(queue)
                        for _ in range(length):
                            cur_i, cur_j = queue.pop(0)
                            if grid1[cur_i][cur_j] == 0:
                                is_sub = False
                            for x, y in directions:
                                new_i = cur_i + x
                                new_j = cur_j + y
                                if 0 <= new_i < n and 0 <= new_j < m and grid2[new_i][new_j] == 1:
                                    grid2[new_i][new_j] = 0
                                    queue.append((new_i, new_j))
                    res = res + 1 if is_sub else res
        return res
