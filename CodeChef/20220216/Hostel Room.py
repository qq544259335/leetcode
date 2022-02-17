for _ in range(int(input())):
    n, init = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    for i in range(n):
        if i == 0:
            nums[i] += init
        else:
            nums[i] += nums[i - 1]
    print(max(max(nums),init))
