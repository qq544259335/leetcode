# https://www.codechef.com/FEB222C/problems/XORPAL
for _ in range(int(input())):
    length = int(input())
    strs = input()
    if length == 1:
        print("Yes")
        continue
    else:
        count = [0] * 2
        for n in strs:
            count[int(n)] += 1
        if length % 2 == 0:
            if (count[0] == count[1]) or (count[0] % 2 == 0 and count[1] % 2 == 0):
                print("Yes")
            else:
                print("No")
        else:
            if (count[1] % 2 == 1 and count[0] % 2 == 0) or (count[0] % 2 == 1 and count[1] % 2 == 0):
                print("Yes")
            else:
                print("No")
