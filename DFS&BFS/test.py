def findPair(profits, target):
    profits = sorted(profits)
    print(profits)
    i , j = 0, len(profits) - 1
    res = set()
    while i != j:
        a= profits[i]
        b = profits[j]
        print(a,b,target)
        if a + b == target:
            print(a,b)
            if (a,b) not in res:
                res.add((a,b))
            i += 1
        elif a +b > target:
            j-=1
        else:
            i += 1
    print(res)
    return len(res)

print(findPair([5,7,9,13,11,6,6,3,3],12))