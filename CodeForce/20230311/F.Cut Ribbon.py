n, a, b, c = list(map(int, input().split()))
cuts = {a, b, c}
dp = [-1] * (n + 1)
dp[0] = 0
for i in range(1, n + 1):
    for cut in cuts:
        if i - cut >= 0:
            dp[i] = max(dp[i], dp[i - cut] + 1) if dp[i - cut] != - 1 else dp[i]
print(dp[-1])
