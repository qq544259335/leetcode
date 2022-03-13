for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    day = 1
    day_dict = {}
    for i in range(1, 31):
        day_dict[i] = day
        day += 1
        if day == 8:
            day = 1
    rest = 8
    for num in nums:
        if day_dict[num] <= 5:
            rest += 1
    print(rest)
