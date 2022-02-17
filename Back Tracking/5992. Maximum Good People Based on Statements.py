class Solution:
    # because backtracking iterates all situation and so does bit masking, so bit masking is also available
    # When everybody is thinking about how to do with the bad guys lies, the really leetcoder choose to skip the bad guys
    def maximumGood(self, statements: [[int]]) -> int:
        n = len(statements)
        res = 0

        def check(permutation):
            for i in range(len(permutation)):
                if permutation[i] == "0":
                    continue
                for j in range(n):
                    if statements[i][j] == 2:
                        continue
                    if (statements[i][j] == 0 and permutation[j] == "1") or (
                            statements[i][j] == 1 and permutation[j] == "0"):
                        return False
            return True

        for i in range(2 ** n, 2 ** (n + 1)):
            permutation = bin(i)[3:]
            if check(permutation):
                res = max(res, permutation.count('1'))
        return res
