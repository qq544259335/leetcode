for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    count_nums = [0] * (n + 1)
    for i in nums:
        count_nums[i] += 1
    mex = -1
    end = False
    for i in range(n + 1):
        if count_nums[i] == 0:
            mex = i
            break
    if mex != -1:
        if mex < min(nums):
            print('Yes')
            continue
        else:
            for i in range(mex):
                if count_nums[i] < 2:
                    print('No')
                    end = True
                    break
            if end:
                continue
            print('Yes')
    else:
        for i in range(n + 1):
            if count_nums[i] < 2:
                print('No')
                end = True
                break
        if end:
            continue
        print('Yes')
