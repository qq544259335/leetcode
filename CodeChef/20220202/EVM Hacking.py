# https://www.codechef.com/START24C/problems/EVMHACK
for _ in range(int(input())):
    inputs = list(map(int, input().split()))
    votes = inputs[:len(inputs)//2]
    totals = inputs[len(inputs)//2:]
    total_votes = 0
    for n in totals:
        total_votes += n
    subs = []
    max_subs = 0
    p_max = -1
    for i in range(len(inputs)//2):
        subs.append(totals[i] - votes[i])
        if subs[i] > max_subs:
            p_max = i
            max_subs = subs[i]
    casted_votes = 0
    for i in range(len(votes)):
        if i != p_max:
            casted_votes += votes[i]
        else:
            casted_votes += totals[i]
    if casted_votes > total_votes /2:
        print("Yes")
    else:
        print("No")

