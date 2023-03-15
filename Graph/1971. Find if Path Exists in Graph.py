from collections import deque


class Solution:
    def validPath(self, n: int, edges: [[int]], source: int, destination: int) -> bool:
        link_map = {}
        for s, d in edges:
            link_map[s] = link_map.get(s, []) + [d]
            link_map[d] = link_map.get(d, []) + [s]
        queue = deque()
        queue.append(source)
        visited = set()
        while queue:
            cur = queue.popleft()
            if cur == destination:
                return True
            nexts = link_map[cur]
            for n in nexts:
                if n in visited:
                    continue
                visited.add(n)
                queue.append(n)
        return False
