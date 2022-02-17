class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        def calculate_cost(target):
            print(target)
            cost = 0
            cur = str(startAt)
            for c in target:
                if cur != c:
                    cost += moveCost + pushCost
                else:
                    cost += pushCost
                cur = c
            print(cost)
            return cost

        if targetSeconds < 60:
            print("situation1")
            return calculate_cost(str(targetSeconds))
        else:
            minutes = targetSeconds // 60
            sec = targetSeconds % 60
            if minutes > 99:
                print("situation4")
                return calculate_cost(str(minutes - 1) + str(sec + 60))
            elif sec + 60 <= 99:
                print("situation2")
                target1 = str(minutes - 1) + str(sec + 60) if minutes > 1 else str(sec + 60)
                target2 = str(minutes) + str(sec) if sec >= 10 else str(minutes) + '0' + str(sec)
                return min(calculate_cost(target1), calculate_cost(target2))
            else:
                print("situation3")
                return calculate_cost(str(minutes) + str(sec) if sec >= 10 else str(minutes) + '0' + str(sec))


test = Solution()
print(test.minCostSetTime(9, 100000, 1, 6039))
