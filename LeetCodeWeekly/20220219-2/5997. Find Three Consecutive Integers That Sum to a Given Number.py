class Solution:
    def sumOfThree(self, num: int) -> [int]:
        if num % 3 != 0:
            return []
        else:
            temp = num // 3
            return [temp - 1, temp, temp + 1]
