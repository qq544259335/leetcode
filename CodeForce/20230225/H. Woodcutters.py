tree_locations = []
tree_heights = []
for _ in range(int(input())):
    nums = list(map(int, input().split()))
    tree_heights.append(nums[1])
    tree_locations.append(nums[0])
dp = [(-1, 'x')] * (len(tree_heights))
dp[0] = (1, 'l')
for i in range(1, len(dp)):
    sub_max, last_direction = dp[i - 1]
    cur = (sub_max, 'x')
    if (i + 1 > len(dp) - 1) or (tree_locations[i] + tree_heights[i] < tree_locations[i + 1]):
        cur = (sub_max + 1, 'r')
    if tree_locations[i] - tree_heights[i] > tree_locations[i - 1]:  # greedily push to left
        if last_direction == 'l' or last_direction == 'x' or last_direction == 'r' and tree_locations[i] - \
                tree_heights[i] > tree_locations[i - 1] + tree_heights[i - 1]:
            cur = (sub_max + 1, 'l')
    dp[i] = cur
print(dp[-1][0])
