class Solution:
    # less space
    def solveNQueensSlow(self, n: int) -> [[str]]:
        res = []
        queens = []

        def backtrack(row):
            if len(queens) == n:
                board = ["." * n] * n
                for qx, qy in queens:
                    board[qx] = board[qx][:qy] + "Q" + board[qx][qy + 1:] if qy < n - 1 else board[qx][:qy] + "Q"
                res.append(board[:])
            for j in range(n):
                can_put = True
                for qx, qy in queens:
                    if not(qx != row and qy != j and (abs(abs(qx) - abs(row)) != abs(abs(qy) - abs(j)))):
                        can_put = False
                        break
                if can_put:
                    queens.append((row, j))
                    backtrack(row + 1)
                    queens.pop(-1)
            return

        backtrack(0)
        return res

    # less time
    def solveNQueens(self, n: int) -> [[str]]:
        res = []
        queens = []
        col_set = set()
        dia_set = set()
        anti_dia_set = set()

        def backtrack(row):
            if len(queens) == n:
                board = ["." * n] * n
                for qx, qy in queens:
                    board[qx] = board[qx][:qy] + "Q" + board[qx][qy + 1:] if qy < n - 1 else board[qx][:qy] + "Q"
                res.append(board[:])
            for j in range(n):
                if j not in col_set and row - j not in dia_set and row + j not in anti_dia_set:
                    can_put = True
                else:
                    can_put = False
                if can_put:
                    queens.append((row, j))
                    col_set.add(j)
                    dia_set.add(row - j)
                    anti_dia_set.add(row + j)
                    backtrack(row + 1)
                    queens.pop(-1)
                    col_set.remove(j)
                    dia_set.remove(row - j)
                    anti_dia_set.remove(row + j)
            return

        backtrack(0)
        return res
test = Solution()
print(test.solveNQueens(4))