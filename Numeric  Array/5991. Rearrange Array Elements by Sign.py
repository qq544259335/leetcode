class Solution:
    def rearrangeArray(self, nums: [int]) -> [int]:
        pos = []
        neg = []
        for i in range(len(nums)):
            if nums[i] < 0:
                neg.append(i)
            else:
                pos.append(i)
        res = []
        for i in range(len(pos)):
            res.append(nums[pos[i]])
            res.append(nums[neg[i]])
        return res