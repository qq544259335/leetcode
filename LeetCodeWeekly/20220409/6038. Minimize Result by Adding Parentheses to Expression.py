class Solution:
    def minimizeResult(self, expression: str) -> str:
        left, right = expression.split('+')
        res_num = float('inf')
        res = ""
        for i in range(len(left)):
            mul1 = left[:i] if i > 0 else "1"
            add1 = left[i:]
            for j in range(len(right)):
                mul2 = right[j + 1:] if j + 1 < len(right) else "1"
                add2 = right[:j + 1]
                num = (int(add1) + int(add2))*int(mul1)*int(mul2)
                print(add1,add2,mul1,mul2)
                print(num)
                if num < res_num:
                    res_num = num
                    temp_left = list(left[:])
                    temp_right = list(right[:])
                    temp_left.insert(i,"(")
                    temp_right.insert(j + 1, ")")
                    res = "".join(temp_left) + "+" + "".join(temp_right)
        return res