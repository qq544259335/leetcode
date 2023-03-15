for _ in range(int(input())):
    n = int(input())
    p = n - 1
    nums = list(map(int, input().split()))
    existed_num = set()
    while p >= 0:
        if nums[p] not in existed_num:
            existed_num.add(nums[p])
        else:
            break
        p -= 1
    print(p + 1)
