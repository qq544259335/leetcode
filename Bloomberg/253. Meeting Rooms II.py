import heapq
class Solution:
    # 5% time 98% space
    def minMeetingRoomsDummy(self, intervals: [[int]]) -> int:
        count = 0
        intervals = sorted(intervals, key=lambda x: x[0])
        while intervals:
            print(intervals, count)
            interval = intervals.pop(0)
            start, end = interval[0], interval[1]
            i = 0
            while i < len(intervals):
                print(start, end)
                if intervals[i][0] >= end:
                    start, end = intervals[i][0], intervals[i][1]
                    print(f"pop{i, intervals[i]}")
                    intervals.pop(i)
                    print(f"after pop{intervals}")
                else:
                    i += 1
            count += 1
            print(f"end{intervals,count}")
        return count


    def minMeetingRooms(self, intervals: [[int]]) -> int:
        rooms = []
        intervals = sorted(intervals, key=lambda x: x[0])
        first = intervals.pop(0)
        heapq.heappush(rooms, first[1])
        while intervals:
            cur = intervals.pop(0)
            if cur[0] >= rooms[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, cur[1])
        return len(rooms)



sol = Solution()
intervals = [[0, 30], [5, 10], [15, 20]]
print(sol.minMeetingRooms(intervals))
