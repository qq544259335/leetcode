class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)
        smaller_than_zero = False
        if numerator * denominator < 0:
            numerator = abs(numerator)
            denominator = abs(denominator)
            smaller_than_zero = True
        int_str = str(numerator // denominator)
        remainder = numerator % denominator
        remainder_set = {}
        pos = 0
        remainder_set[remainder] = pos
        decimals_str = ""
        while True:
            pos += 1
            remainder *= 10
            decimals_str += str(remainder // denominator)
            remainder = remainder % denominator
            if remainder == 0:
                break
            if remainder in remainder_set.keys():
                decimals_str = decimals_str[:remainder_set[remainder]] + "(" + decimals_str[
                                                                               remainder_set[remainder]:] + ")"
                break
            remainder_set[remainder] = pos
        if smaller_than_zero:
            return "-" + int_str + "." + decimals_str
        else:
            return int_str + "." + decimals_str


test = Solution()
print(test.fractionToDecimal(-6, 6))
