n = int(input())
nums = list(map(int, input().split()))
res = 0
has_swap_2 = False
for i in range(len(nums)):
    if i == nums[i]:
        res += 1
    else:
        if not has_swap_2:
            if nums[nums[i]] == i:
                has_swap_2 = True
if has_swap_2:
    print(res + 2)
elif res == n:
    print(res)
else:
    print(res + 1)