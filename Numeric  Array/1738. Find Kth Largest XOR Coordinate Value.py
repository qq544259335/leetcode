class Solution:
    def kthLargestValue(self, matrix: [[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        xor_matrix = []
        topK_heap = [0] * k
        xor_matrix.append([0] * n)
        topK_heap = []
        for i in range(m):
            self.XORCalculatorFast(matrix, i, topK_heap)
        return matrix

    def XORCalculatorFast(self, matrix: [[int]], m: int, topK_heap: [int]):
        n = len(matrix[0])
        xor_line = 0
        for i in range(n):
            xor_line ^= matrix[m][i]
            matrix[m][i] = xor_line ^ matrix[m - 1][i] if m >= 1 else xor_line

    # def XORCalculator(self, matrix: [[int]], m: int, n: int) -> int:
    #     res = 0
    #     for i in range(m + 1):
    #         for j in range(n + 1):
    #             res = res ^ matrix[i][j]
    #     return res
    #


sol = Solution()
matrix = [[5, 2], [1, 6]]
print(sol.kthLargestValue(matrix, 1))
