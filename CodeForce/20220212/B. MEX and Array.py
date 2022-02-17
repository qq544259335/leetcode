for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    res = 0
    for i in range(n):
        for j in range(i, n):
            for k in range(i, j + 1):
                if nums[k] == 0:
                    res += 1
                res += 1
    print(res)