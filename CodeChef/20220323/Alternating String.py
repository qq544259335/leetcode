for _ in range(int(input())):
    n = int(input())
    binary = input()
    count  = [0,0]
    for c in binary:
        count[int(c)] += 1
    big, small = count
    if big == small:
        print(big + small)
    elif big < small:
        small ,big = big,small
        print(small * 2 + 1)
    else:
        print(small * 2 + 1)