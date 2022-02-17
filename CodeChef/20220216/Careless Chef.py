for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    odd = 0
    even = 0
    for n in nums:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
    if odd % 2 ==0 and even % 2== 0:
        print("YES")
    else:
        print("NO")