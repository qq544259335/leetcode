for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    count = 0
    for num in nums:
        if 10 <= num <= 60:
            count += 1
    print(count)
