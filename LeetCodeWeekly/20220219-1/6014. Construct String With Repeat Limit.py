class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        res = ""
        print(count)
        cur = 25
        back = False
        while cur >= 0:
            print(cur, count, back)
            if count[cur] == 0:
                cur -= 1
                continue
            if back:
                print(count[cur], repeatLimit)
                if count[cur] == 0:
                    cur -= 1
                    continue
                count[cur] -= 1
                temp = chr(ord('a') + cur)
                print(temp)
                res += temp
                print(res)
                cur += 1
                while count[cur] == 0:
                    cur += 1
                print(cur, "get back")
                back = False
                continue
            if count[cur] > repeatLimit:
                print(count[cur], repeatLimit)
                count[cur] -= repeatLimit
                temp = chr(ord('a') + cur) * repeatLimit
                print(temp)
                res += temp
                print(res)
                back = True
                cur -= 1
            else:
                print(count[cur])
                temp = chr(ord('a') + cur) * count[cur]
                print(chr(ord('a') + cur), cur, temp)
                res += temp
                print(res)
                count[cur] = 0
                cur -= 1
        return res


test = Solution()
s = "aababab"
repeatLimit = 2
print(test.repeatLimitedString(s, repeatLimit))
