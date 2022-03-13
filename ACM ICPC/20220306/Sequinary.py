seq_num = input()[::-1]
res_float = 0.0
for i in range(len(seq_num)):
    res_float += int(seq_num[i]) * ((3 / 2) ** i)
if res_float.is_integer():
    print(int(res_float))
else:
    n, dec = divmod(res_float, 1)
    n = int(n)
    k, m = dec.as_integer_ratio()
    fraction = str(k)+"/"+str(m)
    print(n, fraction)
