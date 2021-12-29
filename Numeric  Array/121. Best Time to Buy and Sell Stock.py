class Solution:
    #  n n 用了前缀和，不合适了，其实s O(1)可以搞定
    def maxProfit_dumb(self, prices: [int]) -> int:
        if len(prices) == 1:
            return 0
        if len(prices) == 2:
            return 0 if prices[1] - prices[0] < 0 else prices[1] - prices[0]
        sub_list = [0] * (len(prices) - 1)
        res = 0
        max_res = 0
        for i in range(len(sub_list)):
            sub_list[i] = prices[i + 1] - prices[i]
        for num in sub_list:
            if res < 0:
                res = 0
            res += num
            max_res = max(max_res, res)
        return max_res

    # 其实就是顺序下的最大减去最小
    def maxProfit(self, prices: [int]) -> int:
        min_p = 2**31 - 1
        max_p = 0
        for num in prices:
            min_p = min(num, min_p)
            max_p = max(num - min_p, max_p)
        return max_p

sol = Solution()
p = [7,1,5,3,6,4]
print(sol.maxProfit(p))
