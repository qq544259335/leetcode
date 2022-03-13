for _ in range(int(input())):
    length = int(input())
    nums = list(map(int,input().split()))
    a = sum(nums)
    b = 0
    res = max(a,b)
    for i in range(length):
        a -= nums[i]
        b += nums[i]
        res = min(max(a,b),res)
    print(res)