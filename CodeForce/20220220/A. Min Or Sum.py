for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    sum2 = 0
    sum1 = 0
    for nn in nums:
        sum2 = sum2 | nn
        sum1 += nn
    print(min(sum1, sum2))
