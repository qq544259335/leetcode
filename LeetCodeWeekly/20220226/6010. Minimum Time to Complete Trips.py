class Solution:
    # so sexy
    def minimumTime(self, time: [int], totalTrips: int) -> int:
        min_time = 1
        max_time = totalTrips * max(time)
        while min_time <= max_time:
            mid = min_time + (max_time - min_time) // 2
            temp = 0
            for t in time:
                temp += mid // t
            if temp >= totalTrips:
                max_time = mid - 1
            else:
                min_time = mid + 1
        return min_time


test = Solution()
time = [3, 3, 8]
totalTrips = 6
print(test.minimumTime(time, totalTrips))
