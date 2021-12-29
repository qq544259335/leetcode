class Solution:
    def canCompleteCircuit(self, gas: [int], cost: [int]) -> int:
        start = 0
        while start < len(gas):
            gas_now = 0
            for i in range(len(gas)):
                p = (start + i) % len(gas)
                gas_now = gas_now + gas[p] - cost[p]
                if gas_now < 0:
                    start = start + i + 1
                    break
                if i == len(gas) - 1:
                    return start
        return -1


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
sol = Solution()
print(sol.canCompleteCircuit(gas, cost))
