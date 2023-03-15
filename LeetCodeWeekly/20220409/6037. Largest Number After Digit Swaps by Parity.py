class Solution:
    def largestInteger(self, num: int) -> int:
        if len(str(num)) == 1:
            return num
        odd_index = set()
        even_index = set()
        odd = []
        even = []
        num = str(num)
        length = len(num)
        for i in range(len(num)):
            if int(num[i]) % 2 == 0:
                even.append(int(num[i]))
                even_index.add(i)
            else:
                odd.append(int(num[i]))
                odd_index.add(i)
        odd.sort()
        even.sort()
        res = ""
        for i in range(length):
            if i in odd_index:
                res += str(odd.pop(-1))
            else:
                res += str(even.pop(-1))
        return int(res)
