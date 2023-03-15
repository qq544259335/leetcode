# class Solution:
#     def maximumBobPoints(self, numArrows: int, aliceArrows: [int]) -> [int]:
#         dp = [[(0, 0)] * 13 for _ in range(numArrows + 1)]
#         for i in range(numArrows + 1):
#             for j in range(1, 13):
#                 not_get = dp[i][j - 1][0]
#                 if i - (aliceArrows[j - 1] + 1) >= 0:
#                     get = dp[i - (aliceArrows[j - 1] + 1)][j - 1][0] + j - 1
#                 else:
#                     get = -1
#                 if get > not_get:
#                     dp[i][j] = (get, aliceArrows[j - 1] + 1)
#                 else:
#                     dp[i][j] = (not_get, 0)
#         res = []
#         arrow = numArrows
#         print(len(dp), arrow)
#         for d in dp:
#             print(d)
#         for i in range(12, 0, -1):
#             print(arrow,i, dp[arrow][i])
#             if dp[arrow][i][1]:
#                 res.append(dp[arrow][i][1])
#                 arrow -= dp[arrow][i][1]
#             else:
#                 res.append(0)
#         print(dp[-1])
#         res.reverse()
#         res[0] += numArrows - sum(res)
#         return res

class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: [int]) -> [int]:

        def dp(i, j, path):
                not_get = dp(i,j - 1,path)
                if i - (aliceArrows[j - 1] + 1) >= 0:
                    get = dp(i - (aliceArrows[j - 1] + 1), j - 1][0] + j - 1
                else:
                    get = -1
                if get > not_get:
                    dp[i][j] = (get, aliceArrows[j - 1] + 1)
                else:
                    dp[i][j] = (not_get, 0)
        res = []
        arrow = numArrows
        print(len(dp), arrow)
        for d in dp:
            print(d)
        for i in range(12, 0, -1):
            print(arrow, i, dp[arrow][i])
            if dp[arrow][i][1]:
                res.append(dp[arrow][i][1])
                arrow -= dp[arrow][i][1]
            else:
                res.append(0)
        print(dp[-1])
        res.reverse()
        res[0] += numArrows - sum(res)
        return res


sol = Solution()
print(sol.maximumBobPoints(89, [3, 2, 28, 1, 7, 1, 16, 7, 3, 13, 3, 5]))
