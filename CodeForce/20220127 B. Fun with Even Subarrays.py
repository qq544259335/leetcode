for t in range(int(input())):
    length = int(input())
    if length <= 1:
        print(0)
        break
    nums = list(map(int, input().split()))
    # print(length, nums)
    main_num = -1
    res = float('inf')
    start, end = 0, 0
    cur = nums[0]
    max_length = 0
    for i in range(1, length):
        if nums[i] == nums[i - 1]:
            end += 1
        else:
            # print(start, end)
            if end - start + 1 >= max_length:
                max_length = end - start + 1
            start = i
            end = i
            cur = nums[i]
        if i == length - 1:
            # print(start, end)
            if end - start + 1 >= max_length:
                max_length = end - start + 1
            start = i
            end = i
    def calc(start, end):
        temp_res = 0
        while start != 0:
            l = end - start + 1
            n = start - l if start - l >= 0 else 0
            m = end - l if end - l >= 0 else 0
            for j in range(n, m + 1):
                if nums[j] != cur:
                    temp_res += 1
                    break
            start = n
        while end != length - 1:
            l = end - start + 1
            n = start + l if start + l < length else length - 1
            m = end + l if end + l < length else length - 1
            for j in range(n, m + 1):
                if nums[j] != cur:
                    temp_res += 1
                    break
            end = m
        return temp_res


    for i in range(1, length):
        if nums[i] == nums[i - 1]:
            end += 1
        else:
            # print(start, end)
            if end - start + 1 >= max_length:
                max_length = end - start + 1
                res = min(res, calc(start, end))
            start = i
            end = i
            cur = nums[i]
        if i == length - 1:
            # print(start, end)
            if end - start + 1 >= max_length:
                max_length = end - start + 1
                res = min(res, calc(start, end))
            start = i
            end = i
    print(res)
