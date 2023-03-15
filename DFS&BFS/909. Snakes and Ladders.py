from collections import deque
class Solution:
    def snakesAndLadders(self, board: [[int]]) -> int:
        dist = [-1] * len(board) ** 2
        new_graph = [0] * len(board) ** 2
        reverse = 0
        # n**2 n**2
        for i in range(len(board) - 1, -1, - 1):
            temp = list(reversed(board[i])) if reverse else board[i]
            for j in range(len(board)):
                new_graph[(len(board) - i - 1) * len(board) + j] = temp[j]
            reverse = 0 if reverse else 1
        dist[0] = 0
        queue = deque()
        queue.append(0)
        while queue:
            node = queue.popleft()
            for i in range(1, 7):
                if node + i >= len(new_graph):
                    break
                new_node = node + i if new_graph[node + i] == -1 else new_graph[node + i] - 1
                if dist[new_node] != -1:
                    continue
                dist[new_node] = dist[node] + 1
                if new_node < len(new_graph):
                    queue.append(new_node)
        return dist[-1]



sol = Solution()
board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
print(sol.snakesAndLadders(board))