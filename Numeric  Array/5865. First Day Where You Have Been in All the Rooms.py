class Solution:
    def firstDayBeenInAllRoomsStepByStep(self, nextVisit: [int]) -> int:
        timeTable = [0 for _ in range(len(nextVisit))]
        count = -1
        visit = 0
        while True:
            count += 1
            print(visit, count, timeTable)
            timeTable[visit] += 1
            if timeTable[visit] % 2 == 1:
                visit = nextVisit[visit]
            else:
                visit = (visit + 1) % len(nextVisit)
            check = 1
            for i in timeTable:
                check *= i
            if check != 0:
                return count % (7 + 10 ** 9)

    def firstDayBeenInAllRooms(self, nextVisit: [int]) -> int:
        n = len(nextVisit)
        m = 7 + 10 ** 9
        res = [0] * n
        for i in range(1, n):
            res[i] = (res[i - 1] * 2 - res[nextVisit[i - 1]] + 2) % m
        return res[-1]


input = [0, 0, 1, 2, 0, 2, 0, 0]
sol = Solution()
print(sol.firstDayBeenInAllRooms(input))
