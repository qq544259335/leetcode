class Solution:
    # n+Time n 5% 15%
    def jobScheduling(self, startTime: [int], endTime: [int], profit: [int]) -> int:
        comb_list = []
        for i in range(len(startTime)):
            comb_list.append((startTime[i], endTime[i], profit[i]))
        comb_list = sorted(comb_list, key=lambda x: x[0])
        res = 0
        dp = [0] * (max(endTime) + 1)
        start_max = 0
        time = 0
        for i in range(len(comb_list)):
            s, e, p = comb_list[i]
            while time <= s:  # here is the Time, make it slow, because all dp[] are iterated, optimization is below
                start_max = max(start_max, dp[time])
                dp[time] = start_max
                time += 1
            dp[e] = max(dp[e], dp[s] + p)
            res = max(res, dp[e])
        return res
    # nlogn n 15 25
    def jobSchedulingBinarySearch(self, startTime: [int], endTime: [int], profit: [int]) -> int:
        n = len(startTime)
        comb_list = []
        for i in range(len(startTime)):
            comb_list.append((startTime[i], endTime[i], profit[i]))
        comb_list = sorted(comb_list, key=lambda x: x[1])
        comb_list = [(0, 0, 0)] + comb_list  # padding like dp
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            # mean select task i or not, it is better than my original method, which iterate over time, it iterates over n
            # for every dp[i] we have dp[i] = max(dp[i -1], last_chooseable_dp + profit). Chooseable means end time is smaller than start time of dp[i]  so we sort comb_list by end time and use binary search
            # and because last_chooseable_dp k is the optimal of first k so the dp is correct
            l, r = 0, i - 1  # end time k < start time i < end time i
            while l < r:
                mid = (l + r + 1) // 2  # because it start by 0 not 1, so need + 1 to avoid infinite loop
                print(l, mid, r, comb_list[mid][1], comb_list[i][0])
                if comb_list[mid][1] <= comb_list[i][0]:
                    l = mid
                else:
                    r = mid - 1
            dp[i] = max(dp[i - 1], dp[l] + comb_list[i][2])
        return dp[-1]


test = Solution()
startTime = [4, 2, 4, 8, 2]
endTime = [5, 5, 5, 10, 8]
profit = [1, 2, 8, 10, 4]
print(test.jobSchedulingBinarySearch(startTime, endTime, profit))
