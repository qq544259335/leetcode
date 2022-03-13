import copy

target = input()
guess = []
for i in range(7):
    guess.append(input())
pos_dict = {}
for i in range(len(target)):
    if target[i] not in pos_dict:
        pos_dict[target[i]] = set()
    pos_dict[target[i]].add(i)
success = False
for g in guess:
    result = ["X"] * 5
    if success:
        continue
    count_dict = {}
    for k, v in pos_dict.items():
        count_dict[k] = len(v)
    for i in range(len(g)):
        if g[i] in pos_dict and i in pos_dict[g[i]]:
            result[i] = "G"
            count_dict[g[i]] -= 1
    if "".join(result) == "GGGGG":
        success = True
        print("WINNER")
        continue
    for i in range(len(g)):
        if result[i] == "X":
            if g[i] in count_dict and count_dict[g[i]] > 0:
                result[i] = "Y"
                count_dict[g[i]] -= 1
    print("".join(result))
if not success:
    print("LOSER")
