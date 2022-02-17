for _ in range(int(input())):
    n =  int(input())
    nums = list(map(int,input().split()))
    k = 0
    for i in range(n):
        if 1 + i + k == nums[i]:
            k += 1
    print(k)