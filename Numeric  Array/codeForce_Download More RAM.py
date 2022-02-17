for t in range(int(input())):
    length, init = map(int, input().split())
    requirements = list(map(int, input().split()))
    rewards = list(map(int, input().split()))
    r_r_tuples = []
    for i in range(length):
        r_r_tuples.append((requirements[i], rewards[i]))
    r_r_tuples.sort(key=lambda x: x[0])
    mem = init
    while r_r_tuples and mem >= r_r_tuples[0][0]:
        req, rew = r_r_tuples.pop(0)
        mem += rew
    print(mem)

