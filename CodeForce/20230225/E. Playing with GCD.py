for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    if n <= 2:
        print("YES")
        continue
    else:
        p = 0
        while p + 2 <= n - 1:
            if nums[p] == nums[p + 2] and nums[p] != nums[p + 1] and nums[p] % nums[p + 1] == 0 and nums[p + 2] % nums[
                p + 1] == 0:
                break
            else:
                p += 1
    print("YES") if p + 2 > n - 1 else print("NO")
