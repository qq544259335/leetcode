class Solution:
    # 米奇妙妙屋的妙 n 1 https://leetcode-cn.com/problems/find-all-duplicates-in-an-array/solution/shu-zu-zhong-zhong-fu-de-shu-jian-dan-bi-utnm/
    # 有没有出现-> Dict, O(1)空间复杂度 + 数字在1-n之间，在数列内原地做dict
    # 把值变为-num可以在不失去信息的基础上加上visited信息
    def findDuplicates(self, nums: [int]) -> [int]:
        res = []
        for i in range(len(nums)):
            num = abs(nums[i])
            if nums[num - 1] > 0:
                nums[num - 1] = -nums[num - 1]
            else:
                res.append(num)
        return res