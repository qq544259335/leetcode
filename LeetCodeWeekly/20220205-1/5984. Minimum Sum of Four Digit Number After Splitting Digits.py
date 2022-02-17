class Solution:
    def minimumSum(self, num: int) -> int:
        num = str(num)
        nums = []
        for c in num:
            nums.append(int(c))
        nums.sort()
        res = nums[0] * 10 + nums[2] + nums[1] * 10 + nums[3]
        return res