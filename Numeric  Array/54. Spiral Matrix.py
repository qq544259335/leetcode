class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        row = len(matrix[0])
        column = len(matrix)
        directions = [(0, 1), (1, 0), (0, -1), (- 1, 0)]
        cur_dir = 0
        i, j = 0, 0
        VISITED = True
        res = [matrix[i][j]]
        matrix[i][j] = VISITED
        count = row * column - 1
        while count > 0:
            while True:
                new_i = i + directions[cur_dir][0]
                new_j = j + directions[cur_dir][1]
                print(count, new_i, new_j)
                if not (0 <= new_i < column and 0 <= new_j < row):
                    break
                if matrix[new_i][new_j] == VISITED:
                    break
                count -= 1
                res.append(matrix[new_i][new_j])
                matrix[new_i][new_j] = VISITED
                i, j = new_i, new_j
            cur_dir = (cur_dir + 1) % 4
        return res


matrix = [[1,2,3],[4,5,6],[7,8,9]]
test = Solution()
print(test.spiralOrder(matrix))