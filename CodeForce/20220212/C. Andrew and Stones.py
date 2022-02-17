for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    res = 0
    good = True


    def findOdd(j):
        l = - 1
        r = - 1
        for i in range(1, j):
            if nums[i] % 2 == 1:
                l = i
        for i in range(j + 1, n - 1):
            if nums[i] % 2 == 1:
                r = i
        return r, l


    while True:
        all_even = True
        sum_even = 0
        for i in range(1, n- 1):
            sum_even += nums[i]
            if nums[i] % 2== 1:
                all_even = False
                break
        if all_even:
            res += sum_even // 2
            break
        for i in range(1, n - 1):
            if nums[i] >= 2:
                l, r = findOdd(i)
                nums[i] -= 2
                if l != -1:
                    nums[l] += 1
                if r != -1:
                    nums[r] += 1
                res += 1
        end = 0
        bad = 0
        for i in range(1, n - 1):
            if nums[i] == 0:
                end += 1
            elif nums[i] == 1:
                bad += 1
        if end == n - 2:
            break
        if bad + end == n - 2:
            good = False
            break
    if good:
        print(res)
    else:
        print(-1)
