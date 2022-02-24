n = int(input())
nums = list(map(int,input().split()))
check = set()
for num in nums:
    if num not in check:
        check.add(num)
print(len(check))