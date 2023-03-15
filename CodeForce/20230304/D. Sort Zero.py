for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))[::-1]
    zero_set = set()
    min_num = float('inf')
    end = len(nums)
    run = True
    while run:
        for i, num in enumerate(nums[:end]):
            if num in zero_set:
                min_num = 0
            elif min_num >= num:
                min_num = num
            else:
                zero_set = zero_set.union(set(nums[i:]))
                end = i
                min_num = 10 ** 5 + 1
                break
        else:
            run = False
    print(len(zero_set))