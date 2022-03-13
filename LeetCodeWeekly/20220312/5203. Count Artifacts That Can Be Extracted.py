class Solution:
    def digArtifacts(self, n: int, artifacts: [[int]], dig: [[int]]) -> int:
        graph = [[False] * n for _ in range(n)]
        count = 0
        for i,j in dig:
            graph[i][j] = True
        for r1,c1,r2,c2 in artifacts:
            found = True
            for i in range(r1, r2 + 1):
                if not found:
                    break
                for j in range(c1, c2+ 1):
                    if not graph[i][j]:
                        found = False
                        break
            if found:
                count += 1
        return count