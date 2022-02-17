for _ in range(int(input())):
    x = int(input())
    victs = input()
    chef, carl = 0, 0
    for c in victs:
        if c == "D":
            carl += 1
            chef += 1
        elif c == "C":
            carl += 2
        else:
            chef += 2
    if carl == chef:
        print(55 * x)
    elif carl > chef:
        print(60 * x)
    else:
        print(40 * x)
