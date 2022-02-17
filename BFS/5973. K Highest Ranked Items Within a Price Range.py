class Solution:
    def highestRankedKItems(self, grid: [[int]], pricing: [int], start: [int], k: int) -> [[int]]:

        summary = []

        def BFS():
            queue = [start]
            distance = 0
            visited = set()
            visited.add((start[0], start[1]))
            while queue:
                distance += 1
                length = len(queue)
                for i in range(length):
                    i, j = queue.pop(0)
                    if pricing[0] <= grid[i][j] <= pricing[1]:
                        summary.append(([i, j], distance, grid[i][j]))
                    for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        new_i, new_j = i + x, j + y
                        if -1 < new_i < len(grid) and -1 < new_j < len(grid[0]) and grid[new_i][new_j] != 0 and (
                                new_i, new_j) not in visited:
                            queue.append((new_i, new_j))
                            visited.add((new_i, new_j))

        BFS()
        summary.sort(key= lambda x: (x[1], x[2], x[0][0], x[0][1]))
        if len(summary) <= k:
            return [s[0] for s in summary]
        return [summary[i][0] for i in range(k)]