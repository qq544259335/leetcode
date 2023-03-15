length = int(input())
nums = list(map(int, input().split()))
neg = 0
neg_count = 0
zero_count = 0
pos = 0
pos_count = 0
for n in nums:
    if n == 0:
        zero_count += 1
    elif n > 0:
        pos += n
        pos_count += 1
    else:
        neg += n
        neg_count += 1
if neg_count % 2 == 0:
    print(zero_count + pos - pos_count - (neg + neg_count))
else:
    if zero_count == 0:
        print(zero_count + pos - pos_count - (neg + neg_count) + 2)
    else:
        print(zero_count + pos - pos_count - (neg + neg_count))
