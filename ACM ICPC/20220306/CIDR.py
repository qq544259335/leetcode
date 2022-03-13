ips = []
for _ in range(int(input())):
    ips.append(input())
ips_bin = []
for ip in ips:
    ip_bin = ""
    str_nums = ip.split(".")
    for s in str_nums:
        seg = bin(int(s))[2:]
        while len(seg) < 8:
            seg = "0"+seg
        ip_bin += seg
    ips_bin.append(ip_bin)
same_part = ""
for i in range(32):
    cur = ips_bin[0][i]
    flag = False
    for ip in ips_bin:
        if ip[i] == cur:
            continue
        else:
            flag = True
            break
    if flag:
        break
    same_part += "1"
if same_part == "":
    print(32)
else:
    print(len(same_part))