a , b = list(map(int, input().split()))
if a == 1 and b ==  10:
    print("Yes")
    exit()
if b - a == 1:
    print("Yes")
    exit()
print("No")