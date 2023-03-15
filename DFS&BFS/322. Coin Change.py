class Solution:
    # BFS method: key is to save the state and the state is the amount left
    def coinChange(self, coins: [int], amount: int) -> int:
        if amount == 0:
            return 0
        left_set = set()
        queue = [amount]
        level = 0
        while queue:
            level += 1
            new_queue = []
            for change in queue:
                for coin in coins:
                    if change - coin == 0:
                        return level
                    if change - coin > 0 and (change - coin) not in left_set:
                        left_set.add(change - coin)
                        new_queue.append(change - coin)
            queue = new_queue
        return -1

    def coinChangeDP(self, coins: [int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, len(dp)):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[-1] if dp[-1] < float('inf') else -1