class Solution:
    # 脑筋急转弯，，，https://leetcode-cn.com/problems/reverse-integer/solution/zheng-shu-fan-zhuan-by-leetcode-solution-bccn/
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
        rev = 0
        while x != 0:
            if rev < INT_MIN // 10 + 1 or rev > INT_MAX // 10:
                return 0
            digit = x % 10
            if x < 0 and digit > 0:
                digit -= 10
            x = (x - digit) // 10
            rev = rev * 10 + digit
        return rev


sol = Solution()
print(sol.reverse(1534236469))
