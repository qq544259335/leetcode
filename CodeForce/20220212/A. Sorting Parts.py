for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    pre_max_list = [0] * (n - 1)
    pre_max_list[0] = nums[0]
    pos_min_list = [0] * (n - 1)
    pos_min_list[-1] = nums[-1]
    for i in range(1, n - 1):
        pre_max_list[i] = max(pre_max_list[i - 1], nums[i])
    for i in range(n - 2, 0, -1):
        pos_min_list[i - 1] = min(pos_min_list[i], nums[i])
    good = True
    for i in range(n - 1):
        if pre_max_list[i] <= pos_min_list[i]:
            continue
        else:
            good = False
            break
    if good:
        print("no")
    else:
        print("yes")
