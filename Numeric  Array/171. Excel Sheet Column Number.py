class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber != 0:
            columnNumber -= 1
            res += chr(columnNumber % 26 + ord('A'))
            columnNumber = columnNumber // 26
        return res