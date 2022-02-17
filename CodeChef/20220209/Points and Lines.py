for _ in range(int(input())):
    x_set = set()
    y_set = set()
    for _ in range(int(input())):
        x, y = list(map(int, input().split()))
        if x not in x_set:
            x_set.add(x)
        if y not in y_set:
            y_set.add(y)
    print(len(x_set) + len(y_set))
