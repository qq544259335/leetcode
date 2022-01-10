class Solution:
    def openLock(self, deadends: [str], target: str) -> int:
        if "0000" in deadends:
            return -1
        queue = ["0000"]
        visited = set(deadends)
        depth = 0
        while queue:
            length = len(queue)
            for i in range(length):
                cur = queue.pop(0)
                if cur == target:
                    return depth
                for j in range(4):
                    change = cur[j:j + 1]
                    change1 = str((int(change) + 1) % 10)
                    change2 = str((int(change) - 1) % 10)
                    temp1 = cur[:j] + change1 + cur[j + 1:] if j != 3 else  cur[:j] + change1
                    temp2 = cur[:j] + change2 + cur[j + 1:] if j != 3 else  cur[:j] + change2
                    if temp1 not in visited:
                        queue.append(temp1)
                        visited.add(temp1)
                    if temp2 not in visited:
                        queue.append(temp2)
                        visited.add(temp2)
            depth += 1
        return - 1