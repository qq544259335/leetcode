for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    target = 1
    for i in range(n):
        if nums[i] == target:
            target += 1
    print((n - (target - 1)) // k + 1 if (n - (target - 1)) % k != 0 else (n - (target - 1)) // k)
