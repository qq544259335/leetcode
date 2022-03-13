p = float(input())


def get_E(num):
    P = (1 - p) ** num
    return 1 * P + num * (1 - P)


res = float('inf')
res_n = 1
for i in range(1, 17):
    if get_E(i) / i < res:
        res_n = i
        res = get_E(i) / i
print(res_n)
