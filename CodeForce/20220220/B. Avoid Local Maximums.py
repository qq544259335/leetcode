for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.append(0)
    count = 0
    for i in range(1, n - 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            nums[i + 1] = max(nums[i], nums[i + 2])
            count += 1
    print(count)
    for i in range(n):
        nums[i] = str(nums[i])
    print(" ".join(nums[:n]))
