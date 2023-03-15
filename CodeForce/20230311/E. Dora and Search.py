for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    if n < 4:
        print(-1)
    else:
        end = False
        i = 0
        j = n - 1
        max_n = n
        min_n = 1
        while i < j:
            if max_n != nums[i] and max_n != nums[j] and min_n != nums[i] and min_n != nums[j]:
                print(i + 1, j + 1)
                end = True
                break
            elif max_n == nums[i]:
                max_n -= 1
                i += 1
            elif max_n == nums[j]:
                max_n -= 1
                j -= 1
            elif min_n == nums[i]:
                min_n += 1
                i += 1
            elif min_n == nums[j]:
                min_n += 1
                j -= 1
        if not end:
            print(-1)
